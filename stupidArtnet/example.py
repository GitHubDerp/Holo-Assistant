from lib.StupidArtnet import StupidArtnet
import time
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



# THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
target_ip = '192.168.178.81'		# typically in 2.x or 10.x range
universe = 0 					# see docs
packet_size = 300				# it is not necessary to send whole universe

# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
a = StupidArtnet(target_ip, universe, packet_size)

# MORE ADVANCED CAN BE SET WITH SETTERS IF NEEDED
# NET         = DEFAULT 0
# SUBNET      = DEFAULT 0

# CHECK INIT
print(a)

packet = bytearray(packet_size)		# create packet for Artnet


fnt4 = ImageFont.truetype('small_pixel.ttf', 4)
fnt5 = ImageFont.truetype('small_pixel.ttf', 5)
fnt6 = ImageFont.truetype('small_pixel.ttf', 6)
fnt7 = ImageFont.truetype('small_pixel.ttf', 7)
fnt8 = ImageFont.truetype('small_pixel.ttf', 8)
fnt9 = ImageFont.truetype('small_pixel.ttf', 9)
fnt10 = ImageFont.truetype('small_pixel.ttf', 10)
fnt11 = ImageFont.truetype('small_pixel.ttf', 11)
fnt12 = ImageFont.truetype('small_pixel.ttf', 12)

def sendImageToMatrix(img):
	for y in range(10):
		for x in range(10):
			pixel = img.getpixel((x,y)) 
			print(pixel, end='')
			packet[y *30 + x*3]     = pixel[0]
			packet[y *30 + x*3 + 1] = pixel[1]
			packet[y *30 + x*3 + 2] = pixel[2]
		print()
	a.set(packet)
	a.show()

def textToImage(text):
	img = Image.new('RGB', (10, 10))
	d = ImageDraw.Draw(img)
	d.text((0, 0), text, fill=(255, 255, 255), font=fnt7)
	img.save(f'images/{text}.bmp')
	return img

img = textToImage("02")
sendImageToMatrix(img)


# hotfix lib error
a.start()
a.stop()
del a