#Imports
from os import *
from time import *
import subprocess
import threading
from datetime import datetime
from calendar import isleap

timerdict = {}
alarmdict = {}

COMMANDS = ["back","help","wecker","timer","timerlist","delettimer","stopuhr"]

#Wecker underconstruction!
def oneAlarm(delteID,alarmTime):
	while True and deletID:
		if alarmTime == strftime("%X"):
			system('echo "ALARM!!!"')
		wait = False

#Täglich Wecker undercosntruction!
def dailyAlarm(day, month, year, hour, min , name ):
	d = int(strftime("%d"))
	mo = int(strftime("%m"))
	y = int(strftime("%Y"))
	h = int(strftime("%I"))
	m = int(strftime("%M"))
	s = int(strftime("%S"))
	
	
	


	inputvar = input('reuse y/n?')

#Timeddpsn calc.
def calcTimespan(h,m,s):
	timespan = 0.0
	timespan = h*60*60
	timespan = timespan + (m*60)
	timespan = timespan + s
	return timespan

#Timmer
def timer(h,m,s,name):
	timespan = calcTimespan(h,m,s)
	t = threading.Timer(timespan, timerProcess, [name])
	t.start()
	timerdict[name] = t

def timerProcess(name):
	if name in timerdict:
		print(name +"Alarm")
		timerdict[name].cancel()
		timerdict.pop(name)
	else:
		print('eror Timer nicht gefunden')

#Timerlist
def getTimerList():
	for x in timerdict:
		print(x)


#DeletTimer
def deletTimer(name):
	try:
		timerdict.pop(name)	
		print("Timer gelöscht")	
	except:
		print("Timer nicht gefunden")
	



#Stopwatch 
def stopWatch():
	h = int(strftime("%I"))
	m = int(strftime("%M"))
	s = int(strftime("%S"))

	i = input('Stop?')
	h2 = int(strftime("%I"))
	m2 = int(strftime("%M"))
	s2 = int(strftime("%S"))

	t = calcTimespan(h,m,s)
	t2 = calcTimespan(h2,m2,s2)

	timespan = t2 - t
	time = timespan
	min = 0
	hour = 0
	if timespan < 60:
		time = timespan
		block = True
	else:
		while time > 0:
			time = time - 60
			min = min + 1
		if time < 0:
			time = time + 60
			min = min - 1
	while min > 59:
		min = min - 60
		hour = hour + 1
	if min < 59 and block == False:
		min = min + 60
		hour = hour - 1

	print(hour , "Stunden" , min , "Minuten" , time, "Sekunden" )
	
		

#Weckermenue
def Main():
	found = False
	inputvar = input('\033[33mWecker/Timmer/StopUhr\033[0m\n')
	for x in COMMANDS:
		if inputvar == x:
			found = True
			if inputvar == COMMANDS[2]:#Wecker
				inputvar = input('\033[33meinmal/Täglich/nach Wochentag\033[0m\n')
				if inputvar == "einmal":
					print("Noch nicht Verfügbar")
					#inputvarN = input('Name des Alarms:\n')
					#inputvarD = int(input('TT:\n'))
					#inputvarMo = int(input('MM:\n'))
					#inputvarY = int(input('jjjj:\n'))
					#inputvarH = int(input('HH:\n'))
					#inputvarM = int(input('MM:\n'))				
					#oneAlarm(inputvarD, inputvarMo, inputvarJ, inputvarH, inputvarM, inputvarN)
				if inputvar == "täglich":
					print("Noch nicht Verfügbar")
					#inputvarN = input('Name des Alarms:\n')
					#inputvarD = int(input('TT:\n'))
					#inputvarMo = int(input('MM:\n'))
					#inputvarY = int(input('jjjj:\n'))
					#inputvarH = int(input('HH:\n'))
					#inputvarM = int(input('MM:\n'))
					#dailyAlarm(inputvarD, inputvarMo, inputvarY, inputvarH, inputvarM, inputvarN)
			if inputvar == COMMANDS[3]:#timer
				inputvarN = input('Name des Timer:\n')
				inputvarH = int(input('HH:\n'))
				inputvarM = int(input('MM:\n'))
				inputvarS = int(input('SS:\n'))
				timer(inputvarH,inputvarM,inputvarS,inputvarN)
			if inputvar == COMMANDS[4]:#timerlist
				getTimerList()
			if inputvar == COMMANDS[5]:#delettimer
				inputvarN = input('Name des Timer:\n')
				deletTimer(inputvarN)
			if inputvar == COMMANDS[6]:#stopuhr
				stopWatch()
			if inputvar == COMMANDS[0]:#back
				exit()
			if inputvar == COMMANDS[1]:#help
				for x in COMMANDS:
					print('\033[33m'+ x +'\033[0m')
	if found  == False:
		system('echo \033[91m"Falscher Befehl. help for help"\033[0m')
	found = False


#MainLoop
while True:
	Main()
