import docker
#import sys

client = docker.from_env()
#connection between python and docker

#containers contains alll containers running or not
#containers = client.containers.list(all = True)

container = client.containers.get("gameserver-minecraft")


#if len(sys.argv) < 2:
 # print("Usage: python3 docker_controller.py start|etc")
 # sys.exit(1)


#command = sys.argv[1] #this read a command line argument after the fact

def get_status():
  container.reload()
  return {
  "success": True,
  "status": container.status,
  "message": "Container status"
  }

def start_server():
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

def stop_server():
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

def restart_server():
  container.restart()
  container.reload()

  return {
  "success": True,
  "status": container.status,
  "message": "Container restarted"
  }

def get_server_info():
  container.reload()

  return {
  "name": container.name,
  "status": container.status,
  "image": container.image.tags[0]
  }



#print(container.name)
#print(container.status)


#loop through and see every container
#for container in containers:




