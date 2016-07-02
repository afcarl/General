import gdata.youtube
import gdata.youtube.service
import xml.etree.ElementTree as ET
yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True
def GetAuthSubUrl():
  next = 'http://www.example.com/video_upload.pyc'
  scope = 'http://gdata.youtube.com'
  secure = False
  session = True

  yt_service = gdata.youtube.service.YouTubeService()
  return yt_service.GenerateAuthSubURL(next, scope, secure, session)

authSubUrl = GetAuthSubUrl()
print '<a href="%s">Login to your Google account</a>' % authSubUrl

#yt_service = gdata.youtube.service.YouTubeService()


#yt_service.UpgradeToSessionToken(gdata.auth.extract_auth_sub_token_from_url(yt_service.request.url))
# Turn on HTTPS/SSL access.vi
# Note: SSL is not available at this time for uploads.

yt_service.developer_key = 'AIzaSyCc2rYk80b092uXrZkeQy8yIWdjLVSEfAg'
yt_service.client_id = '406084163076-8j46vutbk1tchenhc4ef108ns1ivpsn6.apps.googleusercontent.com'
yt_service = gdata.youtube.service.YouTubeService()
yt_service.email = 'priyakhokher20@gmail.com'
yt_service.password = 'loveprk143'
yt_service.source = 'mood'
yt_service.ProgrammaticLogin()
feed = yt_service.GetYouTubeVideoFeed('http://gdata.youtube.com/feeds/api/standardfeeds/most_viewed')
for entry in feed.entry:
     print entry.statistics.view_count, ' : ', entry.media.title.text




#entry = yt_service.GetYouTubeVideoEntry(video_id='the0KZLEacs')