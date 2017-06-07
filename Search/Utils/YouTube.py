from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

class YouTube(object):
    """docstring for YouTUbe"""
    def __init__(self, arg):
        super(YouTUbe, self).__init__()
        self.arg = arg

    def SummaryService(book):
        # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
        # tab of
        #   https://cloud.google.com/console
        # Please ensure that you have enabled the YouTube Data API for your
        # project.

        print('\n Youtube Videos \n')
        
        DEVELOPER_KEY = "AIzaSyC2AuZ66KtrzM61wX41E7DIGLNa7FMd5H0"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)
        results = []
        # Call the search.list method to retrieve results matching the specified
        # query term.
        try:
            search_response = youtube.search().list(
                q=book + 'book summary',
                part="id,snippet",
                maxResults=3
            ).execute()

            videos = []

            # Add each result to the appropriate list, and then display the lists of
            # matching videos, channels, and playlists.

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    results.append("https://youtube.com/embed/%s" % (search_result["id"]["videoId"]))

                # print("Videos:\n", "\n".join(videos), "\n")
            
        except HTTPError:
            file.writelines("\n\nAn HTTP error %d occurred:\n%s" %
                    (e.resp.status, e.content))
        return results
