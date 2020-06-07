#Imports
from os import *
import time
import subprocess
from Matrix import Matrix
#from _thread import start_new_thread


#FarbCodes
# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKGREEN = '\033[92m'
# YELLOW = '\033[33m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'

#System Stats
LICENSKEY = "none"
LANGUAGE = "German"
SYSTEMVERSION = "HoloAsistant 1.1"

#Commands
NEWCOMMANDS = ["file","dir"]
SYSTEMCOMMANDS = ["shutdown","down","status","new","delete","del","time","date","clock","help"]
OPENCOMMANDS = ["firefox"]

#Matrix
matrix = Matrix(10,10)


#Start
system('echo \033[92m"Holo Asistant ist gestarted"\033[0m')
matrix.startStartupAnimation()



#New file
def newFile(path,name):
	if path != "" and path[-1] != "/":
		path += "/"
	system('touch ' + path+ name)
	print("Datei "+ name +" wurde erstellt. Du findest sie in " + path)
	logNew("File", path + name,"Linux")
	Main()

#New direkt
def newDir(path,name):
	if path != "" and path[-1] != "/":
		path += "/"
	system('mkdir ' + path + name)
	print("Ordner "+ name +" wurde erstellt. Du findest ihn in " + path)
	logNew("Directory",path + name,"Linux")
	Main()

#Commandparser for "new"
def newCommandParser():
	for x in NEWCOMMANDS:
		print('\033[33m',x,'\033[0m')
	inputvar = input('-') #wait for user input
	if inputvar == "back":
		Main()
	if inputvar == "file" or inputvar == "txt":
		inputPfad = input('\033[95mPfad?\033[0m')
		inputName = input('\033[95mName?\033[0m')	
		newFile(inputPfad,inputName)
	if inputvar == "directory" or inputvar== "dir":
		inputPfad = input('\033[95mPfad\033[0m')
		inputName = input('\033[95mName?\033[0m')
		newDir(inputPfad,inputName)



#Delet file
def deleteFile(path):
	system('rm ' + path)
	print(path + " wurde entfernt")
	logDelete("file",path,"Linux")
	Main()

#Delet directory
def deleteDir(path):
	system('rm -r ' + path)
	print(path + " wurde entfernt")	
	logDelete("directory",path,"Linux")
	Main()


#CommandParser for "delete"
def deleteCommandParser():
	for x in NEWCOMMANDS:
		print('\033[33m',x,'\033[0m')
	inputvar = input('-')
	if inputvar == "back":
		Main()
	if inputvar == "file": #file delete
		inputName = input('\033[95mName\033[0m')		
		deleteFile(inputName)
	if inputvar == "directory" or inputvar == "dir": #directory delete
		inputName= input('\033[95mName\033[0m')
		deleteDir(inputName)




#Remembers the created documents
def logNew(typ,path,betriebssystem):
	command = f"create {typ} {path} {betriebssystem} >> DocumentHistory.txt"
	system('echo ' + command)
	Main()

#Remembers the deleted files/Folder
def logDelete(typ,path,betriebssystem):
	command = f"delte {typ} {path} {betriebssystem} >> DocumentHistory.txt"
	system('echo ' + command)
	Main()



#Uhrzeit
def getTime():
	h = time.strftime("%H")
	m = time.strftime("%M")
	s = time.strftime("%S")
	print("Es ist "+ time.strftime("%X"))
	delay = 2
	matrix.sendImageToMatrix(matrix.textToImage(h)) # send to Matrix
	time.sleep(delay)

	matrix.artnet.blackout()
	matrix.sendImageToMatrix(matrix.textToImage(m))
	time.sleep(delay)

	matrix.artnet.blackout()
	matrix.sendImageToMatrix(matrix.textToImage(s))
	time.sleep(delay)
	
	matrix.artnet.blackout()
	Main()

#Datum
def getDate():
	d = time.strftime("%d")
	m = time.strftime("%m")
	y = (time.strftime("%Y"))[-2:]
	print("Heute ist der "+ time.strftime("%d.%m.%Y"))
	delay = 2
	matrix.sendImageToMatrix(matrix.textToImage(d)) # send to Matrix
	time.sleep(delay)

	matrix.artnet.blackout()
	matrix.sendImageToMatrix(matrix.textToImage(m))
	time.sleep(delay)

	matrix.artnet.blackout()
	matrix.sendImageToMatrix(matrix.textToImage(y))
	time.sleep(delay)

	matrix.artnet.blackout()
	Main()



#Clock
def clock():
	system("python3 Clock.py")	


#Status Ausgabe
def statusRep():
	print(" Systemlanguage:",LANGUAGE)#Systemsprache
	print(" Version:",SYSTEMVERSION,"\033[0m")#Version
	print(" LicensKey:\033[91m",LICENSKEY,"\033[0m")#License
	Main()


#Shutdown-Methode
def shutHoloDown():
	system('echo \033[91m"Asistant wird Heruntergefahren"\033[0m')	
	exit()


	

#Main Methode(Menue)
def Main():
	found = False
	inputvar = input('\033[95mMenü\033[0m \n')
	for x in SYSTEMCOMMANDS:
		if inputvar == x:
			found = True
			
			if inputvar == "shutdown" or inputvar == "down":#shutdown
				shutHoloDown()
			if inputvar == "status":#status
				statusRep()
			if inputvar == "new":#new
				newCommandParser()
			if inputvar == "delete" or inputvar == "del":#delete
				deleteCommandParser()
			if inputvar == "time": #Time
				getTime()
			if inputvar == "date": #Date
				getDate()
			if inputvar == "clock": #clock
				clock()
			if inputvar == "help": #help
				for x in SYSTEMCOMMANDS:
					print('\033[33m'+ x +'\033[0m')
	if found  == False:
		system('echo \033[91m"Falscher Befehl. help for help"\033[0m')

#MainLoop
while True:	
	Main()
