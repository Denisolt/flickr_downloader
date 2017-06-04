import flickrapi
from bs4 import BeautifulSoup
import requests
import re
import urllib
import os

<<<<<<< Updated upstream
api_key = raw_input('Enter your API-Key: ')
api_secret = raw_input('Enter your API-Secret: ')
name = raw_input('Enter the username of the desired users pictures: ')
albumID = int(raw_input('Enter the ID of the folder you wish to download: '))

print '\nthe sizes are: \n'+'Square 75 (75 x 75) == sq \n'+'Square 150 (150 x 150) == q\n'+'Thumbnail (67 x 100) == t\n'+'Small 240 (160 x 240) == s\n'+'Small 320 (213 x 320) == n\n'+'Medium 500 (333 x 500) == m\n'+'Medium 640 (427 x 640) == z\n'+'Medium 800 (534 x 800) == c\n'+'Large 1024 (683 x 1024) == l\n'+'Large 1600 (1067 x 1600) == h\n'+'Large 2048 (1365 x 2048) == k\n'
sizes = raw_input('Enter the corresponding letter to the size you would like : ')

counter = 1
flickr = flickrapi.FlickrAPI(api_key, api_secret)
if not os.path.exists('images'):
	os.makedirs('images')
	os.chdir('images')
	for photo in flickr.walk_set(albumID):
	    url = 'https://www.flickr.com/photos/'+ name+ '/' + photo.get('id') + '/sizes/'+ sizes+ '/'
=======

api_key = '78fa534193acf30e53d7c9e95dfdc567'
api_secret = '34160d71501154cd'



counter = 1
flickr = flickrapi.FlickrAPI(api_key, api_secret)
if not os.path.exists('pic'):
	os.makedirs('pic')
	os.chdir('pic')
	for photo in flickr.walk_set('72157629212758502'):
	    url = 'https://www.flickr.com/photos/megane_wakui/' + photo.get('id') + '/sizes/k/'
>>>>>>> Stashed changes
	    webpage = requests.get(url)
	    soup = BeautifulSoup(webpage.text, 'html.parser')
	    x = soup.findAll('img')
	    for link in soup.find_all('img'):
	    	new = (link.get('src'))
	    	if(new.count(".jpg")) == 1:
	    		testfile = urllib.URLopener()
	    		if(photo.get('title') == ''):
	    			counter = counter + 1
	    			testfile.retrieve(new, 'unnamed' + str(counter) + '.jpg' )
	    		else:
	    			testfile.retrieve(new, photo.get('title')+'.jpg')
<<<<<<< Updated upstream
print 'All set, all pictures were downloaded into a folder called images'
=======

print 'All set, all pictures were downloaded into a folder called pics'
>>>>>>> Stashed changes
