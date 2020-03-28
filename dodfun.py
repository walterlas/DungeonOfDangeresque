####           The Dungeon of Dangeresque              ####   
####    (c) 1980 Original by Howard Berenbon           ####
#### Transcribed from:                                 ####
#### Mostly BASIC: Applications for your Atari, Book 2 ####
#### Published by Howard W. Sams & Co., Inc            ####
#### Indianapolis, Indiana 1983                        ####
####             Python Version 1.00                   ####
####         Various Function -- dodfun,py             ####

from os import system, name
from random import random, seed
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

def getDifficulty():
	d	= 0
	while (d < 1) or (d > 2):
		print("Difficulty Level: 1 = Moderate, 2 = Hard")
		n	= input("Enter difficulty level > ")
		d	= int(n)
	return(d)

def getLevels(d):
	numlevels	= d*10
	return(numlevels)

def getIndex(x,y):
	i	=	x+(columns*y)
	return(i)

def getName():
	n	=	input("Enter your character's name > ")
	o	=	str(n)
	return(o)
	
def flourish():				# This needs to be re-done
	for aa in range(1,301):
		print("*        %",end="")
	delay(2)
	print("\n")
#	cls()
	return
	
def createGrid(x,y):
	grid=[]
	for i in range(0,x*y):
		grid.append(i)
	return(grid)

def fillArray(col,row):
	grid	=	createGrid(col,row)
	n		=	0
	for y in range(1,col):
		for x in range(1,row):
			i	= getIndex(x,y)
			grid[i]	= int(rnd()*7+1)
	
	h	=	int(rnd()*3+1)
	for n in range(1,h+1):
		x	=	int(rnd()*col+1)
		y	=	int(rnd()*row+1)
		i	=	getIndex(x,y)
		grid[i]	=	8
	
	s	=	int(rnd()*4+1)+2
	for n in range(1,s+1):
		x	=	int(rnd()*8+1)
		y	=	int(rnd()*8+1)
		i	=	getIndex(x,y)
		grid[i]	=	9
	return(grid)

def fillMap():
	map = []
	n	= 0
	for i in range(0,9*9):
		map.append(i)
	
	for y in range(1,9):
		for x in range(1,9):
			i = x+(9*y)
			map[i] = int(rnd()*7+1)
	h	= int(rnd()*3+1)
	for n in range(1,h+1):
		x	= int(rnd()*8)
		y	= int(rnd()*8)
		i	= x+(9*y)
		map[i]	= 8
	s	= int(rnd()*4+1)+2
	for n in range(1,s+1):
		x	= int(rnd()*8+1)
		y	= int(rnd()*8+1)
		i	= x+(9*y)
		map[i]	= 9
	return(map)
	
def monsterSetup():
# Change this to suppport 3 levels of monsters
	info=[[],[],[]]
	info[0].append(0)
	info[1].append(0)
	info[2].append(0)
	monster=['Large Dragon','Hideous Ghoul','Lizard Man','Manticore','Purple Worm','Deadly Cobra',
			'Mad Elf','Clay Man','Hairy Beast','Mad Dwarf','Zombie','Berserker','Giant Scorpion',
			'Giant Cockroach','Doppleganger','Giant Fire Beetle','Giant Ant','Giant Tick',
			'Mummy','Nasty Orc','Skeleton','Troll','Goblin','Vampire Bat','Creeping Blob',
			'Mad Dog','Large Spider','Black Cat','Man Eating Plant','Hydra','Gelatinous Cube',
			'Giant Centipede','Giant Rat','Shadow']
	monsterhp=[6,5,4,6,6,5,5,4,5,4,4,5,6,4,5,1,1,2,3,2,1,3,3,3,3,2,3,2,1,3,2,1,2,2]
	monsterhm=[12,10,8,12,12,10,10,8,10,8,8,10,12,8,10,2,2,4,6,4,2,6,6,6,6,4,6,4,2,6,4,2,4,4]
	monsterName=" "
	monsterHitPower=0
	monsterStrength=0
	for loop in range(0,34):
		info[0].append(monster[loop])
		info[1].append(monsterhp[loop])
		info[2].append(monsterhm[loop])
	return(info)

## Player Rating ##
## Name - Score - Killed By - Rating
def getRating(r):
	rating = player.name+" - "+str(r)+" - " + player.killedby + " - "
	if (r <= -400):
		rate = "Incompetent serf"
	elif (r <= -100):
		rate = "Weakling"
	elif (r < 0):
		rate = "Apprentice"
	elif (r < 100):
		rate = "Halfling"
	elif (r < 200):
		rate = "Foot soldier"
	elif (r < 600):
		rate = "Warrior"
	elif (r < 900):
		rate = "Great Warrior"
	elif (r < 1500):
		rate = "Swordsman"
	elif (r < 2500):
		rate = "Magic Swordsman"
	elif (r >= 2500):
		rate = "Dungeon Master"
	rating = rating + rate
	return(rating)

def showMap():		# Line 1570 & 1990
	cls()
	if (player.hasmap == False):
		print("You pat your pockets looking for your map")
		print("before you remember you don't have one.")
		delay(1)
	else:
		print(f"The Dungeon of Danger Map: Level {currentlevel}")
		print(" ")
		for q in range(1,9):
			for n in range(1,9):
				if (player.x == n) and (player.y == q):
					print("Pl ",end=" ")
					continue
				else:
					idx = level[currentlevel].getIndex(n,q)
					s1	= level[currentlevel].map[idx]
					if s1 == 1:
						print("O  ",end=" ")
					elif s1 == 2:
						print("C  ",end=" ")
					elif s1 == 3:
						print("M  ",end=" ")
					elif s1 == 4:
						print("M  ",end=" ")
					elif s1 == 5:
						print("?  ",end=" ")
					elif s1 == 6:
						print("NS ",end=" ")
					elif s1 == 7:
						print("EW ",end=" ")
					elif s1 == 8:
						print("?  ",end=" ")
					elif s1 == 9:
						print("UP ",end=" ")
			print("\n")
#	if debug:
#		level[currentlevel].showMap()

	dummy = input("~~Press Enter to Continue~~")
	return	
	
def newGame():
	loop = True
	
	while loop:
		print("Game Over")
		print("Would you like to play again?")
		f = input("Enter (Y)es or (N)o :> ")
		if f.upper() == 'Y' or f.upper() == 'N':
			loop = False
	return(f.upper())

def atWall(dir):
	print(f'You are at the {dir} wall')
	print("You cannot pass through")
	print(" ")
	print("Try another direction?")
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
	initialhp		= 0
	healthturn		= 0
	onlevel			= 0
	deathreason		= " "
	
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
		if playerObject.hp < playerObject.initialhp:
			playerObject.healthturn = playerObject.healthturn + 1
			if playerObject.healthturn > 5:
				playerObject.hp = playerObject.hp + int(rnd()*5)+1
				if playerObject.hp > playerObject.initialhp:
					playerObject.hp = playerObject.initialhp
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

	def didMove():
		if (playerObject.x == playerObject.oldx) and (playerObject.y == playerObject.oldy):
			return False
		else:
			return True
	
	def hasMoved():
		if (playerObject.x == playerObject.oldx) and (playerObject.y == playerObject.oldy):
			return False
		else:
			return True
	
	def upLevel():
		playerObject.haskey = False
		print("Your Enchanted Key melts in the lock!")
		playerObject.hasmap = False
		print("Your map turns to dust!")
		if playerObject.hp < initialHP:
			playerObject.hp = initialHP
			print("You feel stronger. . . . . ")
			delay(1)
			print(f"Your hit-points are restored to {initialHP}")
			print()
		playerObject.monsterskilled	= 0
		print(f"You have gotten to level {currentlevel}")
		delay(2)
		return
	
	def reset(d):
		playerObject.x				=	int(rnd()*8+1)
		playerObject.y				=	int(rnd()*8+1)
		playerObject.startingHP		=	20+(int(rnd()*15)+1)//d
		
		playerObject.movesdepleted	=	False
		playerObject.hasmap			= 	False
		playerObject.haskey			=	False
		
		playerObject.movesleft		=	100
		playerObject.gold			=	500
		playerObject.monsterskilled	=	0
		playerObject.totalkills		=	0
		playerObject.hp				=	playerObject.startingHP
		return

		
class monsterObject:
	name	= 'monster'
	hp		= 1
	hm		= 1
	dead	= False
	
	def decHP(x):
		monsterObject.hp	= monsterObject.hp - x
		if monsterObject.hp <= 0:
			monsterObject.dead = True
		return
	
	def decHM(x):
		monsterObject.hm = monsterObject.hm - x
		if monsterObject.hm <= 0:
			monsterObject.dead = True
		return
		
class levelObject:

	map		= []
	mx		= 9
	my		= 9
	
	def __init__(self):
		return
		
	def createMap():
		for i in range(0,levelObject.mx*levelObject.my):
			levelObject.map.append(i)
		return
	
	def getIndex(x,y):
		i=x+(levelObject.mx*y)
		return(i)

	def getX(i):
		x=i%levelObject.mx
		return(x)

	def getY(i):
		y=i//levelObject.mx
		return(y)

	def getXY(i):
		x=i%levelObject.mx
		y=i//levelObject.mx
		xy=[x,y]
		return(xy)
	
	def showMap():
		index=0
		for ol in range(0,levelObject.mx):
			for il in range(0,levelObject.mx):
				print('{0:2d}'.format(levelObject.map[index]),end=" ")
				index=index+1
			print("\n")
		return

	def roomContents(x,y):
		index = 0
		index = levelObject.getIndex(x,y)
		contents = levelObject.map[index]
		return(contents)
		
	def setMap(x,y,v):
		index = levelObject.getIndex(x,y)
		levelObject.map[index] = v
		return

	def setMapIdx(idx,value):
		levelObject.map[idx]	= value
		return
		
	def fillMap():
		seed()
		n	= 0
		for y in range(1,levelObject.mx):
			for x in range(1,levelObject.my):
				i = levelObject.getIndex(x,y)
				levelObject.map[i] = int(rnd()*7+1)
		
		h	= int(rnd()*3+1)
		
		for n in range(1,h+1):
			x	= int(rnd()*levelObject.mx)
			y	= int(rnd()*levelObject.my)
			i	= levelObject.getIndex(x,y)
			levelObject.map[i]	= 8
		
		s	= int(rnd()*4+1)+2
		
		for n in range(1,s+1):
			x	= int(rnd()*8+1)
			y	= int(rnd()*8+1)
			i	= levelObject.getIndex(x,y)
			levelObject.map[i]	= 9
		return

