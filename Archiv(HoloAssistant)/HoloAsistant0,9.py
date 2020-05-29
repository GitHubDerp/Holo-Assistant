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
SYSTEMCOMMANDS = ["shutdown","status","new","delet","time","date","alarm","execute","help","sudo","comit sudoku"]
OPENCOMMANDS = ["firefox"]
COMMANDS = [[NEWCOMMANDS],[SYSTEMCOMMANDS],[OPENCOMMANDS]]


animStatus = "Idel"


#Startsequenc
#VLCPROCESS = subprocess.Popen(["vlc","--loop","Test.mkv"])
system('echo \033[92m"Holo Asistant ist gestarted"\033[0m')



#openProgramm/file
def execute():
	inputvar = input('\033[33mProgram/Script\033[0m\n')
	if inputvar == "program":
		inputvar = input('\033[95mWelches?\033[0m\n')
		system('' + inputvar)
		Main()
	if inputvar == "script":
		inputvar = input('\033[95mWelches?\033[0m\n')
		system("python3 " + inputvar)
		Main()
	if inputvar == "back":
		Main()



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

#Wecker
def oneAlarm(alarmTime):
	wait = True
	while wait:
		if alarmTime == strftime("%X"):
			system('echo "ALARM!!!"')
			wait = False

#Täglich Wecker
def dailyAlarm():
	sleep(1)#not finished

#Timmer
def timer(h,m,s):
	run = True
	while run:
		system('echo '+str(h)+":"+str(m)+":"+str(s))
		if s > 0:
			s = s - 1
		elif m > 0:
			m = m - 1
			s = 59
		elif h > 0:
			h = h - 1
			m = 59 
		else:
			run = False
		sleep(1)

#Stopwatch
def stopWatch():
	stop = ""
	if stop != " ":
		system('echo '+ str(count))
		sleep(1)
		count = count + 1
		stop = input()
		

#Weckermenue
def alarm():
	inputvar = input('\033[33mWecker/Timmer/StopUhr\033[0m\n')
	if inputvar == "wecker":
		inputvar = input('\033[33meinmal/Täglich/nach Wochentag\033[0m\n')
		if inputvar == "einmal":
			start_new_thread(oneAlarm,(inputvar,))
		if inputvar == "täglich":
			dailyAlarm()
	if inputvar == "timer":
		inputvarH = int(input('HH:\n'))
		inputvarM = int(input('MM:\n'))
		inputvarS = int(input('SS:\n'))
		timer(inputvarH,inputvarM,inputvarS)
	if inputvar == "stopuhr":
		system('echo "underconstruction"')
	if inputvar == "back":
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
	#subprocess.Popen.kill(VLCPROCESS)
	sleep(1)
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
	found = False
	inputvar = input('\033[95mMenü\033[0m \n')
	for x in SYSTEMCOMMANDS:
		if inputvar == x:
			found = True
			
			if inputvar == SYSTEMCOMMANDS[0]:#shutdown
				shutHoloDown()
			if inputvar == SYSTEMCOMMANDS[1]:#stats
				statusRep()
			if inputvar == SYSTEMCOMMANDS[2]:#new
				newCommandParser()
			if inputvar == SYSTEMCOMMANDS[3]:#delet
				deletCommandParser()
			if inputvar == SYSTEMCOMMANDS[4]:#Time
				getTime()
			if inputvar == SYSTEMCOMMANDS[5]:#Date
				getDate()
			if inputvar == SYSTEMCOMMANDS[6]:#Alarm
				alarm()
			if inputvar == SYSTEMCOMMANDS[7]:#Execute
				execute()
			if inputvar == SYSTEMCOMMANDS[8]:#help
				for x in SYSTEMCOMMANDS:
					print('\033[33m'+ x +'\033[0m')
			if inputvar == SYSTEMCOMMANDS[9]:#sudo
				inputvar = input('')
				override(inputvar) 
			if inputvar == SYSTEMCOMMANDS[10]:#comit sudoku
				sudokuEasteregg()
	if found  == False:
		system('echo \033[91m"Falscher Befehl. help for help"\033[0m')
		found = False

#MainLoop
while True:	
	Main()
