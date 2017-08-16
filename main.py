# Python 2.7
import flickrapi
from bs4 import BeautifulSoup
import requests
import re
import urllib
import os



api_key = '78fa534193acf30e53d7c9e95dfdc567'
api_secret = '34160d71501154cd'
flickr = flickrapi.FlickrAPI(api_key, api_secret)

def main():
	if not os.path.exists('images'):
		os.makedirs('images')
	os.chdir('images')
	download()
	print('All set, all pictures were downloaded into a folder called images')

def download():
	choice = (raw_input('Type "tag" or "album" for corresponding choice. \nDo you want to download images by tag or specific album: '))
	#counter is created in order to label the images when they are downloaded
	counter = 0

	if(choice == 'album'):
		albumID = int(raw_input('Enter the ID of the folder you wish to download: '))
		name = raw_input('Enter the username of the desired users pictures: ')
		# checking if the folder exists, creating a folder and moving into it
		if not os.path.exists(name+'/'+albumID):
			os.makedirs(name+'/'+albumID)
		os.chdir(name+'/'+albumID)

		print('Downloading...')
		# walk_set function loops through the pictures of a specific album
		for photo in flickr.walk_set(albumID):
			# beautiful soup opens up the direct link to the picture using authors id(name) and photo id, specifying sizes/k will
			# result in the highest quality picture available on flickr
			url = 'https://www.flickr.com/photos/'+ name+ '/' + photo.get('id') + '/sizes/k/'
			webpage = requests.get(url)
			soup = BeautifulSoup(webpage.text, 'html.parser')
			x = soup.findAll('img')
			# we read the html using soup and look for img, after which we look for src link and extract it
			for link in soup.find_all('img'):
				new = (link.get('src'))
				if(new.count(".jpg")) == 1:
					#the link is downloaded using URLopener() and saved with 'photo + counter'
					testfile = urllib.URLopener()
					testfile.retrieve(new, 'photo' + str(counter) + '.jpg' )
					counter = counter + 1

	elif(choice == 'tag'):
		tag = raw_input('Enter the tags(in format:tagName1,tagName2,tagName3 and etc): ')
		# checking if the folder exists, creating a folder and moving into it
		if not os.path.exists(tag):
			os.makedirs(tag)
		os.chdir(tag)
		# checking the total number of available pictures with the specific tag
		total = int(flickr.photos.search(tags=tag).find('photos').attrib['total'])			
		print('There are ' + str(total) + ' pictures found \nDownloading...')
		# walk_set function loops through the pictures with the tag for more info go to flickrapi python documentation
		for photo in flickr.walk(tag_mode='all', tags=tag):
			author =  photo.get('owner') # return the owner of the picture
			# beautiful soup opens up the direct link to the picture using authors id and photos id, specifying sizes/k will
			# result in the highest quality picture available on flickr
			url = 'https://www.flickr.com/photos/'+ author+ '/' + photo.get('id') + '/sizes/k/'
			webpage = requests.get(url)
			soup = BeautifulSoup(webpage.text, 'html.parser')
			x = soup.findAll('img')
			# we read the html using soup and look for img, after which we look for src link and extract it
			for link in soup.find_all('img'):
				new = (link.get('src'))
				if(new.count(".jpg")) == 1:
					#the link is downloaded using URLopener() and saved with 'photo + counter'
					testfile = urllib.URLopener()
					testfile.retrieve(new, 'photo' + str(counter) + '.jpg' )
					counter = counter + 1
	else:
		print('An Error appeared in your input. ')
		download()


if __name__ == '__main__':
    main()
