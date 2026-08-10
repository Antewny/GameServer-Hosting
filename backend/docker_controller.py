import docker
#import sys

client = docker.from_env()
#connection between python and docker

#containers contains alll containers running or not
#containers = client.containers.list(all = True)

#container = client.containers.get("gameserver-minecraft")


#if len(sys.argv) < 2:
 # print("Usage: python3 docker_controller.py start|etc")
 # sys.exit(1)


#command = sys.argv[1] #this read a command line argument after the fact


def get_container(name):
  return client.containers.get(f"gameserver-{name}")

def list_servers():
    containers = client.containers.list(all=True)

    servers = []

    for container in containers:
        if container.name.startswith("gameserver-"):
            container.reload()

            ports = container.attrs["NetworkSettings"]["Ports"]

            host_port = None

            if ports.get("25565/tcp"):
                host_port = int(
                    ports["25565/tcp"][0]["HostPort"]
                )

            servers.append({
                "name": container.name,
                "status": container.status,
                "port": host_port
            })

    return servers

def find_next_port():

    containers = client.containers.list(all=True)
    used_ports = []
    for container in containers:
        container.reload()
        ports = container.attrs["NetworkSettings"]["Ports"]
        if "25565/tcp" in ports and ports["25565/tcp"] is not None:
            host_port = ports["25565/tcp"][0]["HostPort"]
            used_ports.append(int(host_port))
    port = 25565
    while port in used_ports:

        port += 1

    return port

def create_server(name):
    container_name = f"gameserver-{name}"
    port = find_next_port()
    new_container = client.containers.run(
        "itzg/minecraft-server:latest",
        name=container_name,
        detach=True,
        ports={"25565/tcp": port},
        environment={
            "EULA": "TRUE"
        }
    )

    new_container.reload()

    return {
        "success": True,
        "name": new_container.name,
        "status": new_container.status,
        "port": port,
        "message": "Server created"
    }

def get_status(name):
  container = get_container(name)
  container.reload()
  return {
  "success": True,
  "status": container.status,
  "message": "Container status"
  }

def start_server(name):
  container = get_container(name)
  container.reload()
  if container.status == "running":
    return {
    "success": False,
    "status": container.status,
    "message": "Container already started"
    }

  container.start()
  container.reload()
  
  return {
  "success": True,
  "status": container.status,
  "message": "Container started"
  }

def stop_server(name):
  container = get_container(name)
  container.reload()
  if container.status == "running":
    container.stop()
    container.reload()
  
    return {
    "success": True,
    "status": container.status,
    "message": "Container stopped"
    }
  
  return {
  "success": False,
  "status": container.status,
  "message": "Container already stopped"
  }

def restart_server(name):
  container = get_container(name)
  container.restart()
  container.reload()

  return {
  "success": True,
  "status": container.status,
  "message": "Container restarted"
  }

def get_server_info(name):
  container = get_container(name)
  container.reload()

  return {
  "name": container.name,
  "status": container.status,
  "image": container.image.tags[0]
  }

def get_server_logs(name):
  container = get_container(name)
  logs = container.logs(tail=100)
  #gets most recent 100 log lines

  return {
    "success": True,
    "logs": logs.decode("utf-8"),
#returned as bytes so convert to string 
    "message": "Container logs retrieved"
  }

#print(container.name)
#print(container.status)


#loop through and see every container
#for container in containers:

# if __name__ == "__main__":
  #  print(create_server("creative", 25566))


