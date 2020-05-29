#Imports
from os import *
from time import *
import subprocess

#FarbCodes
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

#Variablen
LICENSKEY = "none"
IDELMODE = True
LANGUAGE = "Deutsch"
systemVersion = "HoloAsistant0,1"
AnimStatus = "Idel"

#VLCPROCESS = subprocess.Popen(["vlc","--loop","Test.mkv"])
system('vlc Test.mkv')
system('echo \033[92m"Holo Asistant ist gestarted"\033[0m')

def statusRep():
	print(" Status:",AnimStatus)#Anim. Status
	print(" Systemlanguage",LANGUAGE)#Systemsprache
	print(" Version:",systemVersion,"\033[0m")#Version
	if LICENSKEY == "none":
		print(" LicensKey\033[91m",LICENSKEY,"\033[0m")#Licens
	else:
		print(" LicensKey\033[92m",LICENSKEY,"\033[0m")

def shutHoloDown():
	#system('vlc EndAnim.mkv')
	system('echo \033[91m"Asistant wird Heruntergefahren"\033[0m')
	sleep(2)	
	#subprocess.Popen.kill(VLCPROCESS)
	exit()


while IDELMODE:
	INPUTVAR = input('\033[95mBefehl?\033[0m \n')
	if INPUTVAR == 'shutdown' or INPUTVAR == 'shdo':
		shutHoloDown()
	if INPUTVAR == 'status?' or INPUTVAR == 'sta':
		statusRep()
			
