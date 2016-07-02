import urllib2
response = urllib2.urlopen('https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=IN&key={AIzaSyCc2rYk80b092uXrZkeQy8yIWdjLVSEfAg}')
html = response.read()