#Imports
from Matrix import Matrix
from os import *
from time import *
import subprocess
import threading
from datetime import datetime
from calendar import isleap

timerdict = {}
alarmdict = {}

matrix = Matrix(10,10)

COMMANDS = ["back","help","timer","timerlist","timerdelete","stopwatch","sw"]


#Timespan calc.
def calcTimespan(h,m,s):
	timespan = 0
	timespan = h*60*60
	timespan = timespan + (m*60)
	timespan = timespan + s
	return timespan

#Timmer
def timer(h,m,s,name):
	timespan = calcTimespan(h,m,s)
	if timespan > 0:
		t = threading.Timer(timespan, timerProcess, [name])
		t.start()
		timerdict[name] = t
	else:
		print("Ungültige Eingabe")	

def timerProcess(name):
	if name in timerdict:
		print("Alarm ausgelöst: " + name)
		timerdict[name].cancel()
		timerdict.pop(name)
		matrix.showAlarm()
	else:
		print('Error Timer nicht gefunden')

#Timerlist
def printTimerList():
	if timerdict:
		for x in timerdict:
			print(x)
	else:
		print("Kein Timer aktiv")


#DeletTimer
def deletTimer(name):
	if name in timerdict:
		timerdict.pop(name)
		print("Timer gelöscht")	
	else:	
		print("Timer nicht gefunden")
	



#Stopwatch 
def stopWatch():
	h = int(strftime("%H"))
	m = int(strftime("%M"))
	s = int(strftime("%S"))

	matrix.startStopwatchAnimation()
	i = input('Stop?')
	matrix.stopStopwatchAnimation()
	
	h2 = int(strftime("%H"))
	m2 = int(strftime("%M"))
	s2 = int(strftime("%S"))

	t = calcTimespan(h,m,s)
	t2 = calcTimespan(h2,m2,s2)

	timespan = t2 - t
	seconds = timespan % 60
	minutes = int((timespan % 3600) / 60)
	hour 	= int(timespan / 3600)
	print(hour , "Stunden" , minutes , "Minuten" , seconds, "Sekunden" )
	



#Weckermenue
def Main():
	found = False
	inputvar = input('\033[33m/Timer/StopUhr\033[0m\n')
	for x in COMMANDS:
		if inputvar == x:
			found = True
			if inputvar == "timer": #timer
				inputvarN = input('Name des Timers:\n')
				inputvarH = int(input('HH: '))
				inputvarM = int(input('MM: '))
				inputvarS = int(input('SS: '))
				timer(inputvarH,inputvarM,inputvarS,inputvarN)
			if inputvar == "timerlist":#timerlist
				printTimerList()
			if inputvar == "timerdelete":#delettimer
				inputvarN = input('Name des Timers:\n')
				deletTimer(inputvarN)
			if inputvar == "stopwatch" or inputvar == "sw":#stopuhr
				stopWatch()
			if inputvar == "back":#back
				exit()
			if inputvar == "help":#help
				for x in COMMANDS:
					print('\033[33m'+ x +'\033[0m')
	if found  == False:
		system('echo \033[91m"Falscher Befehl. help for help"\033[0m')
	found = False


#MainLoop
while True:
	Main()
