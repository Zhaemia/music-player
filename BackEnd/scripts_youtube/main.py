from youtube_api_classes import videoData
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
import json
load_dotenv()


#                    GATHER YT's API DATA CREDENTIALS

SERVICE = os.getenv("SERVICE_NAME")
VERSION = os.getenv("VERSION")
KEY = os.getenv("API_KEY")



#                    Program Start
def main():

    if KEY and SERVICE and VERSION:
        print(True, "Welcome to the youtube program let begin \n\n\n\n\n")
    else: 
        print(False,"\n\n", {"Error": "No Api loaded Program ended......"})
        return 

    video_search_query = (input("Search for youtube video: "))
    videos = videoSearch(video_search_query)
    getVideoID()


def videoSearch(que: str | None) -> list[dict]:
        
    y = build(SERVICE, VERSION, developerKey= KEY)
    request = y.search().list(
        part="snippet",
        q= que,
        maxResults=1
    )
    
    response = request.execute()
    return response

def getVideoID():
    pass



if __name__ == "__main__":

    main()