from fastapi import FastAPI
from .models import Workflow

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/workflows", response_model=Workflow)
def create_workflow(workflow: Workflow):
    return workflow
