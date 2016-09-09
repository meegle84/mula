#!/usr/bin/python

#imports
import sys
import commands
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
image_path_to_upload = "/home/pi/mula/photos_to_upload/"
image_extension = ".jpg"
#size = (640,480)
size = (320,240)
colorspace = "RGB"

while True:
	#get image
	print "Getting Image"
	cam = pygame.camera.Camera("/dev/video0", size)
	cam.start()
	image = cam.get_image()
	cam.stop()
	print "Image Got"
	
	#set name of the image
	status,image_name = commands.getstatusoutput("date '+%F_%H-%M-%S'")
	image_name_with_ext = image_path_to_upload + image_name + image_extension
	
	#save image
	print "Saving Image " + image_name
	pygame.image.save(image, image_name_with_ext)
	
