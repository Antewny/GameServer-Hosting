#this will be for the api communication
#imports fastapi

#allows our front end localhost:5500 to com with api backend
#without browser blocks js req bc front end and back end 
#running dif origins(dif ports/ hosts)

#CORS - cross-origin resource sharing

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from fastapi import FastAPI
from backend.docker_controller import(get_status, get_server_logs, list_servers, 
start_server, stop_server, restart_server, get_server_info, create_server)

class ServerCreateRequest(BaseModel):
  name: str
  port: int



app = FastAPI()

app.add_middleware(
    CORSMiddleware,

#allow these websites to access api
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
#allowing cookies or auth will secure later
    allow_credentials=True,
#allow all htp methods
    allow_methods=["*"],
#allow all req headers from frontend
    allow_headers=["*"],
)

@app.post("/servers")
def create_new_server(server: ServerCreateRequest):
  return create_server(server.name, server.port)

@app.get("/servers")
def servers():
  return list_servers()

#when someone send a GET req to / run func below 
@app.get("/")
def home():
  return {"message": "GameServeHosting API"}


@app.get("/servers/{name}/status")
def status(name: str):
  return get_status(name)

#name: str is a hint saying name will be a string

@app.post("/servers/{name}/start")
def start(name: str):
  return start_server(name)

@app.post("/servers/{name}/stop")
def stop(name: str):
  return stop_server(name)

@app.post("/servers/{name}/restart")
def restart(name: str):
  return restart_server(name)

@app.get("/servers/{name}/info")
def info(name: str):
  return get_server_info(name)

@app.get("/servers/{name}/logs")
def logs(name: str):
  return get_server_logs(name)
