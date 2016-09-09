#!/usr/bin/python

#imports
import sys
import commands
import os
from twython import Twython
from twython import TwythonError

#keys
CONSUMER_KEY = 'AeM7V8nSW07jOOnAGoJ3SBnry'
CONSUMER_SECRET = 'UYsRBhtGscFILWTq6HC4REFz924lVi6EIYk73AxDmbPeI3oWyy'
ACCESS_KEY = '2616085993-xDVvNBQwywb6txJ6Jdq0uyDcCELPQmqxZdCwuZE'
ACCESS_SECRET = 'v4iE0zplPL1of03TlbyskGvjXyDGnuQVY683UkU06eknK'

#constants
firsthashtag = "#LaMulaSQV "
hashtags = ["#11AnysDeCorrebars","#BarraquesSQV2015","#PUKN","#SQVViuICombatiu","#LaImpremta","#MamaSurtoALaFoto"]
image_path_to_upload = "/home/pi/mula/photos_to_upload/"
image_path_uploaded = "/home/pi/mula/uploaded_photos/"

while True:
        for hashtag in hashtags:
                #get image
		image_list = sorted(os.listdir(image_path_to_upload))
		if len(image_list) > 0:
			image_name = image_path_to_upload + image_list[0]

                	#open image
                	photo = open(image_name, 'rb')

                	#status text
                	status_text = firsthashtag + hashtag

                	try:
				#auth
				api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
                	except TwythonError as e:
				print e
				pass
			else:
				try:
					#send image to twitter acount
                		        api.update_status_with_media(media=photo, status=status_text)
                		except TwythonError as error:
                       		 	print "ERROR: Image " + image_name + " with hashtags " + status_text + " NOT SENT"
                        		print error
					pass
                		else:
                        		print "Image " + image_name + " sent with hashtags " + status_text
					commands.getoutput("mv " + image_name + " " + image_path_uploaded)
		else:
			print "No images to upload in " + image_path_to_upload

