# dodfun.py
# Functions for Dungeons of Doom
# that are helpful.
from os import system, name
from random import random
from time import sleep

debug = False

def delay(seconds):
	if debug == False:
		sleep(seconds)
	return

def cls():
	if debug == False:
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')
	return
	
def rnd():
	return(random())

def showFile(filename):
	file	= open(filename,'r')
	msg		= file.read()
	file.close()
	print(msg)
	return
	
class playerObject:
	name			= 'name'
	hp				= 1
	x				= 0
	y				= 0
	oldx			= 0
	oldy			= 0
	gold			= 500
	turnstaken		= 0
	turnsleft		= 100
	monsterskilled	= 0
	totalkills		= 0
	haskey			= False
	hasmap			= False
	dead			= False
	movesdepleted	= False
	startinghp		= 0
	healthturn		= 0
	
	def decHP(x):
		playerObject.hp = playerObject.hp - x
		if playerObject.hp <= 0:
			playerObject.dead = True
		return
	
	def incHP(x):
		playerObject.hp = playerObject.hp + x
		return
	
	def turnEnd():
		playerObject.turnstaken = playerObject.turnstaken + 1
		playerObject.turnsleft	= playerObject.turnsleft - 1
		if playerObject.turnsleft == 0:
			playerObject.movesdepleted = True
		if playerObject.hp < playerObject.startinghp:
			playerObject.healthturn = playerObject.healthturn + 1
			if playerObject.healthturn > 5:
				playerObject.hp = playerObject.hp + int(rnd()*5)+1
				if playerObject.hp > playerObject.startinghp:
					playerObject.hp = playerObject.startinghp
					print("You feel like your old self again.")
				else:
					playerObject.healthturn = 0
					print("You're feeling slightly better.")
		else:
			playerObject.healthturn = 0
		return
		
	def move(c,d):
#		playerObject.turnstaken = playerObject.turnstaken + 1
#		playerObject.turnsleft	= playerObject.turnsleft - 1
		playerObject.oldx		= playerObject.x
		playerObject.oldy		= playerObject.y
		playerObject.x			= c
		playerObject.y			= d
		return

class monsterObject:
	name	= 'monster'
	hp		= 1
	hm		= 1
	dead	= False
	
	def decHP(x):
		monsterObject.hp	= monsterObject.hp - x
		if monsterObject.hp <= 0:
			dead = True
		return

class levelObject:

	map		= []
	mx		= 9
	my		= 9
	
	def __init__(self):
		return
		
	def createMap(self):
		for i in range(0,self.mx*self.my):
			self.map.append(i)
		return
	
	def getIndex(self,x,y):
		i=x+(self.mx*y)
		return(i)

	def getX(self,i):
		x=i%self.mx
		return(x)

	def getY(self,i):
		y=i//self.mx
		return(y)

	def getXY(self,i):
		x=i%self.mx
		y=i//self.mx
		xy=[x,y]
		return(xy)
	
	def showMap(self):
		index=0
		for ol in range(0,self.mx):
			for il in range(0,self.mx):
				print('{0:2d}'.format(self.map[index]),end=" ")
				index=index+1
			print("\n")
		return

	def roomContents(self,x,y):
		index = 0
		index = self.getIndex(x,y)
		contents = self.map[index]
		return(contents)
		
	def setMap(self,x,y,v):
		index = self.getIndex(x,y)
		self.map[index] = v
		return

	def setMapIdx(self,idx,value):
		self.map[idx]	= value
		return
		
	def fillMap(self):
		n	= 0
		for y in range(1,self.mx):
			for x in range(1,self.my):
				i = self.getIndex(x,y)
				self.map[i] = int(rnd()*7+1)
		
		h	= int(rnd()*3+1)
		
		for n in range(1,h+1):
			x	= int(rnd()*self.mx)
			y	= int(rnd()*self.my)
			i	= self.getIndex(x,y)
			self.map[i]	= 8
		
		s	= int(rnd()*4+1)+2
		
		for n in range(1,s+1):
			x	= int(rnd()*8+1)
			y	= int(rnd()*8+1)
			i	= self.getIndex(x,y)
			self.map[i]	= 9
		return

