from fastapi import FastAPI
from agent_tools import create_folder


app = FastAPI()

@app.get("/")
def root():
    result = create_folder.invoke({
        "folder_name" : "chh" 
    })
    return {
        "message" : "alright",
        "result" : result
    }