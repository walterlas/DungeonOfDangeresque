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

def attackMonster():
	global monster
	
	cls()
	delay(1)
	print(f"You attack the. . . {monster.name}")
	delay(1)
	print("With a swing of your sword")
	n	= int(rnd()*5+1)+int(rnd()*player.monsterskilled/2+1)
	monster.decHM(n)
	if monster.dead:
		deadMonster()
		return(monster.hm)
	print(f"You do {n} hit-points of damage")
	delay(1)
	print(f"It has . . {monster.hm} hit-points left")
	delay(1)
	return(monster.hm)
	
def flee():
	global player
	
	w	= int(rnd()*4+1)
	player.x	= player.oldx
	player.y	= player.oldy
	print("You decide to make a strategic withdrawal. . . ")
	if teleportactive:
		teleportTrap()
	n	= int(rnd()*2+1)
	delay(1)
	if (w >= 3):
		player.decHP(n)
		print(f"As you leave. . . ")
		print(f"the {monster.name} attacks")
		delay(1)
		print(f"And it does {n} hit-points of damage")
		delay(1)
	return
	
def fightOrFlee():
	print("")
	f = input("Will you (F) or (R)un? ")
	return(f)
	
def doBattle():
	battleloop	= True
	delay(1)
	print(" ")
	w	= int(rnd()*4+1)
	if (w > 2):
		monsterAttacks()
		if player.dead:
			battleloop = False
			return
	while battleloop:
		f	= fightOrFlee()
		if f.upper() == 'F':
			check	= attackMonster()
			if (check <= 0):
				battleloop = False
				continue
			else:
				monsterAttacks()
				if player.dead:
					battleloop = False
					return
		else:
			flee()
			battleloop = False
	return
	
def occupiedCavern():
	global monster
	
	if (inroom == 4):
		w	= int(rnd()*15+1)+15
	else:
		w	= int(rnd()*15+1)
	
	print("There is something lurking. . . ")
	print(". . . . in this chamber . . . . ")
	delay(1)
	print(". . . . . . . . . Beware")
	delay(1)
	print("")
	monster.name	= monsterInfo[0][w]
	monster.hp		= monsterInfo[1][w]
	monster.hm		= monsterInfo[2][w]
	print(f"It is a . . . . . {monster.name} . . ")
	delay(1)
	doBattle()
	return
	
def emptyChamber():
	w	= int(rnd()*2+1)
	if (w == 2):
		print("You are in a damp and misty. . . . ")
		print(". . . . empty chamber.")
	else:
		print("You are in a cold and dark. . . . ")
		print(". . . . empty chamber.")
	return
	
def findVial():
	global player
	
	print("You look around . . . ")
	delay(2)
	v	= int(rnd()*7+1)
	if (v < 5):
		print(". . . but you don't see anything interesting.")
	else:
		print("On the ground, at your feet, is a vial.")
		delay(2)
		print("You pick up the vial. . and see that")
		print("It contains . . . a milky liquid.")
		Print("Would like a drink?")
		d	= input("Enter (Y)es or (N)o: ")
		dl	= int(rnd()*6+)
		if d.upper() == 'N':
			print("You think maybe drinking strange 'milky' liquids")
			print("in strange vials lying on the ground is a bad ")
			print("idea and you put it down.")
			return
		else:
			print("You take a swig. . . ")
			delay(3)
			if (dl >= 3):
				h	= int(rnd()*10/difficulty+1)+(6/difficulty)
				h	= int(h)
				player.incHP(h)
				print("It was a white magic potion. . . ")
				print(f"Which restored you hit-points by {h}")
			elif (dl == 2):
				print("The liquid has no effect on you.")
			else:
				h	= int(rnd()*6+1)*difficulty
				h	= int(h)
				player.decHP(h)
				print("You feel a little funny. . . ")
				delay(2)
				print("\nIt was a black magic potion. . .")
				print(f"Which decreased your hit-points by {h}.')
				if player.dead:
					print("It kind of killed you.")
		return

def somethingJumps():
	cls()
	print("Suddenly. . . Something jumps. . . ")
	print("in front of you . . . . . ")
	delay(2)
	return
		
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
		elif (inroom == 2):		# Hidden Cavern
			hiddenCavern()
		elif (inroom ==3 ) or (inroom == 4):
			occupiedCavern()
