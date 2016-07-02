import numpy as np 
import pandas as pd 
import wget
import urllib 
for i in range(1):
	text_file = open('buzzfeed_food.txt','w')
	f = urllib.urlopen("http://www.buzzfeed.com/api/v2/feeds")
	text_file.write(f.read())
	text_file.close()
	
	# filename = wget.download(url)
	# print filename