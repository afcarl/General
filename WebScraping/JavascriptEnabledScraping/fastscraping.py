
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from PIL import Image
import pylab as pl
import urllib, cStringIO

import numpy as np

driver = webdriver.PhantomJS("C:\Users\priya\Downloads\phantomjs-2.1.1-windows/\/bin\phantomjs.exe")
driver.get("http://207.251.86.238/cctv261.jpg?rand=0.8980015057204902")
time.sleep(3)
html = driver.page_source
#print html
soup = BeautifulSoup(html,"lxml")
print soup
#print soup.find_all("img",{'id':"myPic"})['src']
# URL1 = [x['src'] for x in soup.find_all("img",{'id':"myPic"})]

# URL = URL1[0]
# file1 = cStringIO.StringIO(urllib.urlopen(URL).read())
# img = Image.open(file1)
# img.show()


