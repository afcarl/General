#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCc2rYk80b092uXrZkeQy8yIWdjLVSEfAg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  #print options
  new_response_list = []
  image_urls_list = []
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    #chart="mostPopular",
    maxResults=1,
    regionCode="US"
  ).execute()
  new_response =  youtube.playlistItems().list(
    part="id,snippet",
    maxResults=1,

    playlistId="PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-"
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    # elif search_result["id"]["kind"] == "youtube#playlist":
    #   playlists.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                 search_result["id"]["playlistId"]))

  #print videos#"Videos:\n", "\n".join(videos), "\n"
  # print 
  #print channels# "Channels:\n", "\n".join(channels), "\n"
  #print "Playlists:\n", "\n".join(playlists), "\n"
  #these
  print new_response
  
  for i in range(1):
    try:
      new_response_list.append(new_response['items'][i]['snippet']['resourceId']['videoId'])
      image_urls_list.append(new_response['items'][i]['snippet']['thumbnails']['default']['url'])
      print new_response
    except:
      pass  
  new_response_list = new_response_list 

  #print new_response_list  

  print videos
  #these

  image_urls(image_urls_list)
  

def image_urls(image_urls_list):
  print image_urls_list


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Popular Right Now - UnitedStates")
  argparser.add_argument("--max-results", help="Max results", default=1 )
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

