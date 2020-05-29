#Imports
from os import *
from time import *
import subprocess

#FarbCodes
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
YELLOW = '\033[33m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

#System Stats
LICENSKEY = "none"
IDELMODE = True
LANGUAGE = "Deutsch"
SYSTEMVERSION = "HoloAsistant0,5"

#Commands
NEWCOMMANDS = ["Datei","Ordner"]
SYSTEMCOMMANDS = ["shutdown","status","new","delet"]
COMMANDS = [[NEWCOMMANDS],[SYSTEMCOMMANDS]]


animStatus = "Idel"

#Startsequenc
#VLCPROCESS = subprocess.Popen(["vlc","--loop","Test.mkv"])
system('echo \033[92m"Holo Asistant ist gestarted"\033[0m')

#CommandParser for "new"
def newCommandParser():
	for x in NEWCOMMANDS:
		print('\033[33m',x,'\033[0m')
	inputvar = input('-')
	if inputvar == "back":
		Main()
	if inputvar == NEWCOMMANDS[0] or inputvar == "TXT":
		inputPfad = input('pfad')		
		newFile(inputPfad)
	if inputvar == NEWCOMMANDS[1] or inputvar== "dir":
		inputPfad = input('\033[95mpfad\033[0m')
		newDir(inputPfad)

#NewFile
def newFile(pfad):
	system('touch ' + pfad)
	print("Datei wurde erstellt. Du findest sie in" + pfad)
	Main()

#NewDirekt
def newDir(pfad):
	system('mkdir ' + pfad)
	print("Ordner wurde erstellt. Du findest ihn in" + pfad)
	Main()

#DeletFile
def deletFile(pfad):
	print("under construction")	
	Main()

#Status Ausgabe
def statusRep():
	print(" Status:",animStatus)#Anim. Status
	print(" Systemlanguage:",LANGUAGE)#Systemsprache
	print(" Version:",SYSTEMVERSION,"\033[0m")#Version
	if LICENSKEY == "none":
		print(" LicensKey:\033[91m",LICENSKEY,"\033[0m")#Licens
	else:
		print(" LicensKey:\033[92m",LICENSKEY,"\033[0m")
	Main()


#Shutdown-Methode
def shutHoloDown():
	#system('vlc EndAnim.mkv')
	system('echo \033[91m"Asistant wird Heruntergefahren"\033[0m')
	sleep(2)	
	#subprocess.Popen.kill(VLCPROCESS)
	exit()

#Main Methode(Menue)
def Main():
	inputvar = input('\033[95mBefehl?\033[0m \n')
	if inputvar == "help":
		for x in SYSTEMCOMMANDS:
			print('\033[33m'+ x +'\033[0m')
	if inputvar == SYSTEMCOMMANDS[0] or inputvar == 'shd':#shutdown
		shutHoloDown()
	if inputvar == SYSTEMCOMMANDS[1] or inputvar == 'sta':#stats
		statusRep()
	if inputvar == SYSTEMCOMMANDS[2]:#new
		newCommandParser()
	if inputvar == SYSTEMCOMMANDS[3]:#delet
		print("under construction try later")

#MainLoop
while True:	
	Main()
