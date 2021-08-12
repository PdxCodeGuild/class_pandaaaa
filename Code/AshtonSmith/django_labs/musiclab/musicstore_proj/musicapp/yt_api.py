

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
def yt_search(search_term):
    api_key = load_dotenv()
    token = os.getenv('TOKEN')
    youtube = build('youtube', 'v3', developerKey=token)
    request = youtube.search().list(
        part="snippet",
        order="relevance",
        # status.embeddable =True,
        q=search_term,
    )
    response = request.execute()
    return response




