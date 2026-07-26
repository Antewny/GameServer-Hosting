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
  return container.status

def start_server():
  contqiner.reload()
  if container.status == "running":
    return "The container is already running"

  container.start()
  container.reload()
  
  return "The container is now running"

def stop_server():
  container.reload()
  if container.status == "running":
    container.stop()
    container.reload()
  
    return "The container has been stopped"
  
  return "The container is already stopped"

def restart_server():
  container.restart()
  container.reload()

  return "The container has been restarted"

#print(container.name)
#print(container.status)


#loop through and see every container
#for container in containers:




