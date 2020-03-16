## Dungeon of Dangeresque
## Re-factor

## Imports ##
from random import random
from os 	import system,name
from time	import sleep
from dodfun	import cls,rnd,delay,playerObject,monsterObject,levelObject,showFile

## Variables ##
level	= [1]
player	= playerObject
monster	= monsterObject

debug	= True
newgame	= True
onload	= True
gameloop= True

difficulty	= 1
maxlevels	= 10

def giantSpider():
	global monster

	monster.name = 'Giant Spider'
	monster.hp   = 6
	monster.hm   = 12
	print("It's a huge man-sized crawling")
	print(". . . . . . SPIDER . . . . . . ")
	delay(2)
	print(". . . . . . and . . . . . . ")
	doBattle()
	return
	
def mrWizard():
	global player

	print("Halt! I am the Ancient Wizard")
	print("I will not harm you . . . . .")
	delay(2)
	print("")
	gold = int(rnd()*300+1)+100
	player.gold = player.gold + gold
	print("")
	print(f"I givee you . . . {gold} gold pieces")
	print("out of good will and friendship.")
	print("")
	hp = int(rnd()*10/difficulty+1)+(6/difficulty)
	player.inHP(hp)
	print("Also, I will increase . . . ")
	print(f"your hit-points by {hp}.")
	delay(2)
	return

def darkWizard():
	global monster

	monster.name	= 'Dark Wizard'
	monster.hp		= 8
	monster.hm		= 14

	cls()

	print(f"Do not pass!  I am the {monster.name}")
	delay(2)
	print("And I will hack you to pieces . . . ")
	delay(1)
	doBattle()
	return

def hiddenCavern():
	if player.hasmoved:
		print("You have stunbled onto . . . . . ")
	else:
		print("You are in . . . . . ")
	print("A hidden cavern.")
	if player.hasmoved != True:
		return
	delay(2)
	print("")
	findVial()
	if player.dead:
		print("Unforunately, the swig of that potion has poisoned")
		print("you.")
		playerDead()
	w = int(rnd()*9+1)
	if w > 3:
		print("The cavern seems empty. . . ")
		return
	delay(2)
	print("But wait. . .  before you proceed")
	delay(1)
	print("")
	print("You hear a noise off in the distance")
	delay(1)
	print("Cautiously, you walk towards the sound.")
	delay(2)
	w = int(rnd()*4+1)
	somethingJumps()
	if (w == 1) and (player.hp < player.startinghp):
		mrWizard()
	elif (w == 2):
		giantSpider()
	elif (w == 4) and (currentlevel > 1):
		fallInPool()
	else:
		darkWizard()
	return


## Main Loop ##
while gameloop:
	if onload:
		introTop()
		monsterInfo	= monsterSetup()
		for i in range(1,maxlevels+1):
			level.append(levelObject())
		onload = False
	
	if newgame:
		introMiddle()
		currentlevel	= maxlevels
		for i in range(1,maxlevels):
			level[i].createMap()
			level[i].map	= fillMap()
		
		player.x	= int(rnd()*8+1)
		player.y	= int(rnd()*8+1)
		level[currentlevel].setMap(player.x,player.y,1)
		
		difficulty				= int(getDifficulty())
		teleportactive			= False
		player.movesdepleted	= False
		player.hasmap			= False
		player.haskey			= False
		player.movesleft		= 100
		player.gold				= 500
		player.startinghp		= 20+int(rnd()*15+1)
		player.startinghp		= player.startinghp//difficulty
		targetkills				= int(rnd()*4+1)+4
		player.monsterskilled	= 0
		player.totalkills		= 0
		player.name				= getName()
		player.hp				= player.initialhp
		
		delay (2)
		introBottom()
		inroom					= level[currentlevel].roomContents(player.x,player.y)
		newgame					= False
	
#		cls()

##	Show what room player is in 
		if (inroom == 1):		# Empty chamber
			emptyChamber()		# 	Nothing happens here
		if (inroom == 2):		# Hidden Cavern
			hiddenCavern()

