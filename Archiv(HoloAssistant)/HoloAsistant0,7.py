#Imports
from os import *
from time import *
import subprocess
from _thread import start_new_thread

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
SYSTEMCOMMANDS = ["shutdown","status","new","delet","time","date","alarm"]
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
		inputPfad = input('\033[95mPfad?\033[0m')
		inputName = input('\033[95mName?\033[0m')	
		newFile(inputPfad,inputName)
	if inputvar == NEWCOMMANDS[1] or inputvar== "dir":
		inputPfad = input('\033[95mPfad\033[0m')
		inputName = input('\033[95mName?\033[0m')
		newDir(inputPfad,inputName)

#NewFile
def newFile(pfad,name):
	system('touch ' + pfad+ name)
	print("Datei "+name+" wurde erstellt. Du findest sie in" + pfad)
	rememNew("File",name,"Linux")
	Main()

#NewDirekt
def newDir(pfad,name):
	system('mkdir ' + pfad + name)
	print("Ordner "+name+" wurde erstellt. Du findest ihn in" + pfad)
	rememNew("Folder",name,"Linux")
	Main()



#CommandParser for "delet"
def deletCommandParser():
	for x in NEWCOMMANDS:
		print('\033[33m',x,'\033[0m')
	inputvar = input('-')
	if inputvar == "back":
		Main()
	if inputvar == NEWCOMMANDS[0]:#datei delet
		inputName = input('\033[95mName\033[0m')		
		deletFile(inputName)
	if inputvar == NEWCOMMANDS[1]:#ordner delet
		inputName= input('\033[95mName\033[0m')
		deletDir(inputName)

#DeletFile
def deletFile(name):
	system('rm ' + name)
	print(name," wurde entfernt")	
	Main()

#DeletOrdner
def deletDir(name):
	system('rmdir ' + name)
	print(name," wurde entfernt")	
	Main()



#Remembers the made documents
def rememNew(typ,dateinname,betriebssystem):
	system('echo '+ typ +" "+ dateinname + " " + betriebssystem + '>> DocumentHistory.txt')
	Main()

#Remembers the deleted files/Folder
def rememDelet(typ,dateinname,betriebssystem):
	system('echo '+ typ +" "+ dateinname + " " + betriebssystem + '>> DeletHistory.txt')
	Main()



#Uhrzeit
def getTime():
	print("Es ist "+ strftime("%X"))
	Main()

#Datum
def getDate():
	print("Heute ist der "+ strftime("%d")+"."+strftime("%m")+"."+strftime("%Y"))
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


def sudokuEasteregg():
	print("What NOOOO i dont't want it ")
	inputvar = input('really?')
	if inputvar == "yes":
		print("As you command. SUDOKU!!!!")
		sleep(10)
		#Blackscreen
		print("Not really")
		Main()
	elif inputvar == "no":
		print("thank you <3")
		Main()

def override(code):
	if code == "HAOR-22102k19-ALPHA":
		print("Rasberie backdor")
		Main()
	else:
		print('\033[93m'+"False code"+'\033[0m')
		Main()
	

#Main Methode(Menue)
def Main():
	inputvar = input('\033[95mBefehl?\033[0m \n')
	if inputvar == "help":
		for x in SYSTEMCOMMANDS:
			print('\033[33m'+ x +'\033[0m')
	if inputvar == "comit sudoku":
		sudokuEasteregg()
	if inputvar == "sudo":
		inputvar = input('')
		override(inputvar)
	if inputvar == SYSTEMCOMMANDS[0] or inputvar == 'shd':#shutdown
		shutHoloDown()
	if inputvar == SYSTEMCOMMANDS[1] or inputvar == 'sta':#stats
		statusRep()
	if inputvar == SYSTEMCOMMANDS[2]:#new
		newCommandParser()
	if inputvar == SYSTEMCOMMANDS[3]:#delet
		deletCommandParser()
	if inputvar == SYSTEMCOMMANDS[4] or inputvar == "Uhrzeit":#Time
		getTime()
	if inputvar == SYSTEMCOMMANDS[5] or inputvar == "Datum":#Date
		getDate()
	if inputvar == SYSTEMCOMMANDS[6]:#Alarm
		alarm()
#MainLoop
while True:	
	Main()
