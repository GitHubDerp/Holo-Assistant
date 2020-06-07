from stupidArtnet.lib.StupidArtnet import StupidArtnet
import time
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import threading

class Matrix:
    def __init__(self,dimX, dimY):
        # THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
        target_ip = '192.168.43.15'		# typically in 2.x or 10.x range
        universe = 0 					# see docs
        packet_size = dimX * dimY * 3	# it is not necessary to send whole universe

        self.dimX = dimX
        self.dimY = dimY
        self.artnet = StupidArtnet(target_ip, universe, packet_size)
        self.packet = bytearray(packet_size)		# create packet for Artnet
        self.fnt7 = ImageFont.truetype('stupidArtnet/small_pixel.ttf', 7)
        self.fnt8 = ImageFont.truetype('stupidArtnet/small_pixel.ttf', 8)
        self.stopwatchAnimator = None

    def sendImageToMatrix(self, img):
        for y in range(self.dimY):
            for x in range(self.dimX):
                pixel = img.getpixel((x,y)) 
                self.packet[y *3 * self.dimY + x*3]     = pixel[0] #R
                self.packet[y *3 * self.dimY + x*3 + 1] = pixel[1] #G
                self.packet[y *3 * self.dimY + x*3 + 2] = pixel[2] #B
        self.artnet.set(self.packet)
        self.artnet.show()

    def textToImage(self,text):
        img = Image.new('RGB', (self.dimX , self.dimY))
        d = ImageDraw.Draw(img)
        d.text((0, 1), text, fill=(255, 255, 255), font= self.fnt8)
        #img.save(f'stupidArtnet/images/{text}.bmp')
        return img

    def showColor(self,r,g,b):
        for y in range(self.dimY):
            for x in range(self.dimX):
                self.packet[y *3 * self.dimY + x*3]     = r #Red
                self.packet[y *3 * self.dimY + x*3 + 1] = g #Green
                self.packet[y *3 * self.dimY + x*3 + 2] = b #Blue
        self.artnet.set(self.packet)
        self.artnet.show()

    def startStopwatchAnimation(self):
        self.stopwatchAnimator = self.StopwatchAnimator(self, 0,255,0)
        self.stopwatchAnimator.start()

    def stopStopwatchAnimation(self):
        if self.stopwatchAnimator != None:
            self.stopwatchAnimator.stop = True
            self.stopwatchAnimator.join()
            self.stopwatchAnimator = None

    class StopwatchAnimator (threading.Thread):
        def __init__(self, matrix, r, g, b,):
            threading.Thread.__init__(self)
            self.r = r
            self.g = g
            self.b = b
            self.matrix = matrix
            self.animationPixels = [(4,3),(5,3),(6,4),(6,5),(5,6),(4,6),(3,5),(3,4)]
            self.stop = False
            
        def run(self):
            index = 0
            while not self.stop:
                for y in range(self.matrix.dimY):
                    for x in range(self.matrix.dimX):
                        if (x,y) in self.animationPixels and self.animationPixels.index((x,y)) != index:
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3]     = self.r #Red
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 1] = self.g #Green
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 2] = self.b #Blue
                        else:
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3]     = 0 #Red
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 1] = 0 #Green
                            self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 2] = 0 #Blue
                self.matrix.artnet.set(self.matrix.packet)
                self.matrix.artnet.show()
                time.sleep(0.2)
                
                if index < len(self.animationPixels) - 1:
                    index += 1
                else:
                    index = 0
            self.matrix.artnet.blackout()


    class myAlarm (threading.Thread):
        def __init__(self, matrix, r, g, b,flashcount = 5):
            threading.Thread.__init__(self)
            self.r = r
            self.g = g
            self.b = b
            self.flashcount = flashcount
            self.matrix = matrix
            
        def run(self):
            while self.flashcount > 0:
                self.matrix.showColor(255,0,0)
                time.sleep(1)
                self.matrix.artnet.blackout()
                time.sleep(1)
                self.flashcount -= 1

    # matrix only supports 16 steps
    def showAlarm(self):
        showAlarmThread = self.myAlarm(self, 255,0,0)
        showAlarmThread.start()

    class StartAnimation (threading.Thread):
        def __init__(self, matrix):
            threading.Thread.__init__(self)
            self.matrix = matrix
            
        def run(self):
            g = 0
            b = 0
            for y in range(self.matrix.dimY):
                for x in range(self.matrix.dimX):
                    self.matrix.packet[y *3 * self.matrix.dimY + x*3]     = 0 #Red
                    self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 1] = g #Green
                    self.matrix.packet[y *3 * self.matrix.dimY + x*3 + 2] = b #Blue
                g += 25
                b += 25
                self.matrix.artnet.set(self.matrix.packet)
                self.matrix.artnet.show()
                time.sleep(0.5)
            self.matrix.artnet.blackout()

    def startStartupAnimation(self):
        startAnimation = self.StartAnimation(self)
        startAnimation.start()
        startAnimation.join()
        self.artnet.blackout()



    # hotfix lib error
    #artnet.start()
    #artnet.stop()
    #del artnet