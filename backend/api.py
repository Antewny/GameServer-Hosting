#this will be for the api communication
#imports fastapi

#allows our front end localhost:5500 to com with api backend
#without browser blocks js req bc front end and back end 
#running dif origins(dif ports/ hosts)

#CORS - cross-origin resource sharing

from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from backend.docker_controller import(get_status, get_server_logs, 
start_server, stop_server, restart_server, get_server_info)

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

#when someone send a GET req to / run func below 
@app.get("/")
def home():
  return {"message": "GameServeHosting API"}


@app.get("/status")
def status():
  return get_status()

@app.post("/start")
def start():
  return start_server()

@app.post("/stop")
def stop():
  return stop_server()

@app.post("/restart")
def restart():
  return restart_server()

@app.get("/info")
def info():
  return get_server_info()

@app.get("/logs")
def logs():
  return get_server_logs()
