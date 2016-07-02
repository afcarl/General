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
  
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    #chart="mostPopular",
    maxResults=25,
    regionCode="CA"
  ).execute()
  new_response =  youtube.playlistItems().list(
    part="id,snippet",
    maxResults=2,

    playlistId="PLp12xt0S4J0VS2-7wjO2TWPzLpcnqAANa"
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
    if search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  # print videos#"Videos:\n", "\n".join(videos), "\n"
  # # print 
  # print channels# "Channels:\n", "\n".join(channels), "\n"
  #print "Playlists:\n", "\n".join(playlists), "\n"
  for i in range(2):
    print new_response['items'][i]['snippet']['title']


  print new_response['items'][1]['snippet']['title']


if __name__ == "__main__":
  
  args = {'q':'Popular Right Now - Canada','auth_host_name':'localhost', 
  'auth_host_port':[8080, 8090], 'logging_level':'ERROR', 'max_results':25, 'noauth_local_webserver':False}

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

