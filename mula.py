#imports
import sys
import commands
import pygame
import pygame.camera
from pygame.locals import *
from twython import Twython

#keys
CONSUMER_KEY = '1ZeDMQg0x1AQTrEaG5XyiT9hD'
CONSUMER_SECRET = 'jDnQ6edrW62M5eComGpSyuQPsE9Ka8fhzx0w9prVWRs7N7o4wc'
ACCESS_KEY = '2616085993-xDVvNBQwywb6txJ6Jdq0uyDcCELPQmqxZdCwuZE'
ACCESS_SECRET = 'v4iE0zplPL1of03TlbyskGvjXyDGnuQVY683UkU06eknK'

#auth
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

#constants
firsthashtag = "#LaMulaSQV "
hashtags = ["#11AnysDeCorrebars","#BarraquesSQV2015","#PUKN","#SQVViuICombatiu","#LaImpremta","#MamaSurtoALaFoto"]
image_path = "./fotos/"
image_extension = ".jpg"

#inits
pygame.init()
pygame.camera.init()

while True:
	for hashtag in hashtags:
		#get image
		cam = pygame.camera.Camera("/dev/video0",(640,480))
		cam.start()
		image = cam.get_image()
		cam.stop()
	
		#set name of the image
		status,image_name = commands.getstatusoutput("date '+%F_%H-%M-%S'")
		image_name_with_ext = image_path + image_name + image_extension
	
		#save image
		pygame.image.save(image, image_name_with_ext)
	
		#open image
		photo = open(image_name_with_ext,'rb')
		print "Image " + image_name + " saved"		

		#status text
		status_text = firsthashtag + hashtag
		
		#send image to twitter acount
		api.update_status_with_media(media=photo, status=status_text)
		print "Image " + image_name + " sent with hashtags " + status_text
			
