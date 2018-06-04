import sys
import os
import commands
import cv2
import time
import imageio
import glob

from twython import Twython, TwythonError
from datetime import datetime
from ConfigParser import SafeConfigParser

mypwd = os.path.dirname(os.path.realpath(__file__))
imagespath = mypwd + '/images/'
extension = '.png'
gifname = 'animated.gif'


def get_image(capture):
	ret, image = capture.read()
	print 'new image captured'
	return image


def save_image(image):
	filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	cv2.imwrite(imagespath + filename + extension, image)
	print 'image ' + filename + ' saved to disk'


def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	imageio.mimsave(imagespath + gifname, images, duration=duration)
	print 'gif ' + gifname + ' saved to disk'


def delete_images(filenames):
	for filename in filenames:
		os.remove(filename)
		print 'image ' + filename + ' deleted'


def list_images():
	images = glob.glob(imagespath + '*' + extension)
	return images


def upload_media(filename):
	parser = SafeConfigParser()
	parser.read('config.cfg')
	parser

	CONSUMER_KEY = parser.get('KEYS', 'CONSUMER_KEY')
	CONSUMER_SECRET = parser.get('KEYS', 'CONSUMER_SECRET')
	ACCESS_KEY = parser.get('KEYS', 'ACCESS_KEY')
	ACCESS_SECRET = parser.get('KEYS', 'ACCESS_SECRET')
	api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

	hashtags = parser.get('HASHTAGS', 'hashtags')

	photo = open(filename, 'rb')
	try:
		response = api.upload_media(media=photo)
		api.update_status(status=hashtags, media_ids=[response['media_id']])
		print "Image " + filename + " sent with hashtags " + hashtags
	except TwythonError as e:
		print e


if __name__ == "__main__":
	script = sys.argv.pop(0)

	if len(sys.argv) < 2:
		print('Usage: python {} <number of images to capture> <capture source>'.format(script))
		sys.exit(1)


	imagestocapture = int(sys.argv.pop(0))
	source = int(sys.argv.pop(0))

	capture = cv2.VideoCapture(source)
	capture.set(3, 320)
	capture.set(4, 240)
	for i in range(imagestocapture):
		save_image(get_image(capture))
		time.sleep(1)

	create_gif(list_images(), 1)
	delete_images(list_images())
	upload_media(imagespath + gifname)
