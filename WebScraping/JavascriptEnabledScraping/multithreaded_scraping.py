from selenium import webdriver
import time
from bs4 import BeautifulSoup
from PIL import Image
import pylab as pl
import urllib, cStringIO
from urllib import urlretrieve
import numpy as np
import timeit
from Queue import Queue 
from threading import Thread


driver = webdriver.PhantomJS("C:\Users\priya\Downloads\phantomjs-2.1.1-windows/\/bin\phantomjs.exe")
driver.get("http://207.251.86.238/cctv261.jpg?rand=0.993656320748411")
time.sleep(3)
html = driver.page_source
#print html
soup = BeautifulSoup(html,"lxml")
#print soup.find_all("img",{'id':"myPic"})['src']
URL1 = [x['src'] for x in soup.find_all("img")]
img_list = [0]*500
URL = URL1[0]
print 'started'
print id(img_list)
i = 0
def save_image(q,i):
	
	while True:
		i = i+1
		imges = q.get()
		imges.save(str(i)+'.jpg')
		q.task_done()
		





if __name__ == '__main__':

	i = 0
	q = Queue(maxsize=0)
	num_threads = 1
	for i in range(num_threads):
		worker = Thread(target=save_image, args=(q,i))
		worker.setDaemon(True)
		worker.start()
		
	for i in range(500):
		try:
			time.sleep(0.25)
			file1 = cStringIO.StringIO(urllib.urlopen(URL).read())
			print file1
			break
			#img = Image.open(file1)
			q.put(Image.open(file1))
			
			

		except:
			time.sleep(5)
			pass
	

