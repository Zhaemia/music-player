from youtube_api_classes import videoData
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
import json
import yt_dlp




#                    GATHER YT's API DATA CREDENTIALS
load_dotenv()
yt_link = "https://www.youtube.com/watch?v="
SERVICE = os.getenv("SERVICE_NAME")

VERSION = os.getenv("VERSION")

KEY = os.getenv("API_KEY")




#Search for a list of videos using youtubeDATA api v3 to generate a list of videos to choose from.
def videoSearch(que: str | None) -> list[dict]:

    #Empty placeholder list
    videos_list = []

    #Run youtubs API to generate vidoes from search param "q"
    y = build(SERVICE, VERSION, developerKey= KEY)

    request = y.search().list(
        part="snippet",
        q= que,
        maxResults=5,
        type = 'video'
    )

    #execute HTTPS response 
    response = request.execute()

    #if none drawback and end program for now
    if response is None:
        return "No videos found"

    #Pull the information from our response but only grab whats inside of 'items'
    items: list[dict] = response['items']

    #loop items and append to our previously initiated videos list
    for item in items: 
        videos_list.append({'id': item['id']['videoId'], "title": item['snippet']['title'] })

    #return our new list of dictionaries. keys: id , title
    return videos_list





def getVideoID(video_id: list[dict]) -> str:

    #Enumerate to generate well visible list selection
    for i, item in enumerate(video_id, start=1):
       print(i, item)

    #Gather video selection
    video_selection = int(input("Select video by number: "))

    #Return that videos title and id for now
    return video_id[video_selection - 1].get('id'), video_id[video_selection - 1].get('title')





def streamVideo(vID):

    return




#                    Program Start
def main():

    #Check if our APIS are loaded if not end program for now.
    if KEY and SERVICE and VERSION:
        print(True, "Welcome to the youtube program let begin \n\n")

    else: 
        print(False,"\n\n", {"Error": "No Api loaded Program ended......"})
        return

     
    video_search_query = (input("Search for youtube video: "))

    videos = videoSearch(video_search_query)
    
    selected_video_id = getVideoID(videos)
    if not selected_video_id:
        return {"Error": "Couldnt generate video Id.... Program exit."}
    
    print(selected_video_id)
    
if __name__ == "__main__":

    main()