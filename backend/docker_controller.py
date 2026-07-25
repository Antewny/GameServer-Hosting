import docker
import sys

client = docker.from_env()
#connection between python and docker

#containers contains alll containers running or not
#containers = client.containers.list(all = True)

container = client.containers.get("gameserver-minecraft")


if len(sys.argv) < 2:
  print("Usage: python3 docker_controller.py start|etc")
  sys.exit(1)


command = sys.argv[1] #this read a command line argument after the fact

if command == "start":
  container.start()
  container.reload()
  print("You have started the container")

elif command == "stop":
  container.stop()
  container.reload()
  print("You have stopped the container")

elif command == "restart":
  container.restart()
  container.reload()
  print("You have restarted the container")

elif command == "status":
  container.reload()
  print(f"Status: {container.status}") 




#container.start()
#container.reload() #update make sure old data is not being read

#print(sys.argv[1])

print(container.name)
print(container.status)


#loop through and see every container
#for container in containers:




