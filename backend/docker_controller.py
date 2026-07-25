import docker


client = docker.from_env()
#connection between python and docker

#containers contains alll containers running or not
containers = client.containers.list(all = True)

#loop through and see every container
for container in containers:
  print(container.name, container.status)



