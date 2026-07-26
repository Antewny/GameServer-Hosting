#this will be for the api communication
#imports fastapi
from fastapi import FastAPI
from backend.docker_controller import get_status, start_server, stop_server, restart_server

app = FastAPI()

#when someone send a GET req to / run func below 
@app.get("/")
def home():
  return {"message": "GameServeHosting API"}


@app.get("/status")
def status():
  return {"status": get_status()}

@app.post("/start")
def start():
  return {"start": start_server()}

@app.post("/stop")
def stop():
  return {"stop": stop_server()}

@app.post("/restart")
def restart():
  return {"restart": restart_server()}

