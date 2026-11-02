#To: run uvicorn main:app --reload

from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
api_key = os.getenv("API_KEY")


app = FastAPI()

class VideoMeta(BaseModel):
    id: str
    title: str
    channel: str
    thumbnail: str




@app.get("/")
async def home():
    return("Hello")

#Test current API status
@app.get("/keytest")
async def get_env_key():
    if api_key is None:
        return {False: "API KEY IS NOT ACTIVE"}
    return {True: "API KEY is up and working"}

