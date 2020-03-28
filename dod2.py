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
columns		= 9

def yesNo():
	print("")
	f = input("Enter (Y)es or (N)o > ")
	return(f.upper)
	
def getMap():
	print("You search the chamber and")
	delay(1)
	print("You . . . . . find a map of the level.")
	player.hasmap = True
	return

def findFleeExit():
	global player

	exitfind = True
	while exitfind:
		r=int(rnd()*4+1)
		if (r == 1): # Check North
			if ((player.y - 1) > 0 and (inroom != 7)):
				player.oldy = player.y -1
				exitfind = False
			else:
				continue
		if (r == 3): # Check South
			if ((player.y + 1 < 9) and (inroom != 7)):
				player.oldy = player.y + 1
				exitfind = False
			else:
				continue
		if (r == 2): # Check East
			if (player.x + 1 < 9) and (inroom != 6):
				player.oldx = player.x + 1
				exitfind = False
			else:
				continue
		if (r == 4): # Check West
			if (player.x - 1 > 0) and (inroom != 6):
				player.oldx = player.x - 1
				exitfind = False
			else:
				continue
	return

def getDifficulty():			#Line 5530
	difficulty	= 0
	while (difficulty < 1) or (difficulty > 2):
		print("Difficulty Level: 1 = Moderate, 2 = Hard")
		n = input("Enter difficulty level > ")
		difficulty = int(n)
	return(n)

def getLevels():
	deep	= 0
	while deep == 0:
		levels=input("How many levels deep do you want to start? ")
		levels=int(levels)
		if (levels >0) and (levels <= 5):
			deep = 1
	return(levels)

def getIndex(x,y):
	i=x+(columns*y)
	return(i)

def createGrid(x,y):
	grid=[]
	for i in range(0,x*y):
		grid.append(i)
	return(grid)

#def fillArray(col,row):
#	grid	= createGrid(col,row)
#	n		= 0
#	for y in range(1,col):
#		for x in range(1,row):
#			i = getIndex(x,y,col)
#			grid[i] = int(rnd()*7+1)	# Returns 1-7
#	
#	h	= int(rnd()*3+1)				# Returns 1-3
#	
#	for n in range(1,h+1):
#		x	= int(rnd()*col)
#		y	= int(rnd()*row)
#		i	= getIndex(x,y,col)
#		grid[i]	= 8		# Trap doors?
#		
#	s	= int(rnd()*4+1)+2
#
#	for n in range(1,s+1):
#		x	= int(rnd()*8+1)
#		y	= int(rnd()*8+1)
#		i	= getIndex(x,y,col)
#		grid[i]	= 9		# Stairs Up?
#	return(grid)
	
def fillMap(lvl):
	global level

#	seed()
	n	= 0
	for y in range(1,9):
		for x in range(1,9):
#			i = level[lvl].getIndex(x,y)
			i = getIndex(x,y)
			level[lvl] = int(rnd()*7+1)
		
	h	= int(rnd()*3+1)
	
	for n in range(1,h+1):
		x	= int(rnd()*9)
		y	= int(rnd()*9)
		i	= getIndex(x,y)
		level[lvl]	= 8
		
	s	= int(rnd()*4+1)+2
		
	for n in range(1,s+1):
		x	= int(rnd()*8+1)
		y	= int(rnd()*8+1)
		i	= getIndex(x,y)
		level[lvl]	= 9
	return
	
def getName():
	n = input("Enter your character's name > ")
	o = str(n)
	return(o)

def monsterSetup():
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
	
def	intoPit():
	global pitfall
	global player
	
	print("You fell into a deep . . . pit")
	delay(1)
	print("Luckily . . you didn't get hurt")
	print(" ")
	delay(1)
	print("But in climbing out . . . ")
	print("You . . . . . . lost")
	print("all of your gold pieces.")
	print(" ")
	player.gold = 0
	if player.haskey:
		print("But . . . you still have your key")
	return
	
def trapDoor():
	global currentlevel
	global player
	
	print("You activated a . . . trap door")
	delay(2)
	trap = int(rnd()*4+1)*difficulty
	
	if (trap > 4):
		print("You fell thru . . . ")
		delay(1)
		print("And it killed you.")
		player.dead = True
		player.deathreason = "Broken neck"
		return
	elif (trap == 4):
		if (currentlevel > 1):
			intoPit()
			return
		currentlevel = currentlevel + 1
		if (currentlevel > maxlevel):
			currentlevel = maxlevel
		print(" ")
		print(f"You fell thru to level {currentlevel} . . . and")
		delay(1)
		print("you . .  . . . . . lost")
		print("all of your gold pieces")
		player.gold = 0
		if (player.haskey):
			print("But you still have your key!")
		return
	else:
		print("But . . . you caught yourself")
		print("from falling")
		return
	return
	
def inCorridor():
	global monster
	global player
	
	w	= int(rnd()*8+1)
	if (w >= 7):
		w	= int(rnd()*4+1)+30
		monster.name	= monsterInfo[0][w]
		monster.hp		= monsterInfo[1][w]
		monster.hm		= monsterInfo[2][w]
		
		print("There is something lurking")
		print("in this corridor . . . ")
		delay(1)
		print(". . . . Beware")
		delay(1)
		print(f"\nIt is a . . . . . {monster.name} . . ")
		delay(1)
		doBattle()
		return
	w	= int(rnd()*8+1)
	if (w == 8):
		if player.haskey == False:
			player.haskey == True
			print("\nYou notice a shiny object . . . . ")
			print(". . . . at your feet")
			delay(1)
			print("You pick it up and find that . . . ")
			print("It is the enchanted key . . . . . ")
			delay(1)
			print("\nBut you weren't careful . . . . ")
			delay(1)
		print("You activated some sort of trap . . . ")
		delay(1)
		player.x = int(rnd()*8+1)
		player.y = int(rnd()*8+1)
#		player.oldx = player.x
#		player.oldy = player.y
		player.move(player.x,player.y)
		print("Suddenly you feel dizzy, and pass out")
		delay(2)
		flourish()
		print("When you wake up . . . you find")
		print("that you were . . . . teleported")
		print("to an unknown location . . . . ")
		delay(2)
		findFleeExit()
	return
	
def nsCorridor():
	cls()
	print("You are in a North-South corridor")
	print("You can only go North or South.")
	if player.hasMoved() == False:
		return
	if (player.x - 1 == player.oldx) or (player.x +1 == player.oldx):
		print("The door closes and locks behind you")
	inCorridor()
	return

def ewCorridor():
	cls()
	print("You are in an East-West corridor")
	print("You can only go East or West.")
	if player.hasMoved() == False:
		return
	if (player.y+1 == player.oldy) or (player.y-1 == player.oldy):
		print("The door closes and locks behind you")
	inCorridor()
	return
	
def thief():
	global player
	global level
	
	cls()
	print("There is a thief in this chamber")
	idx	= level[currentlevel].getIndex(player.x,player.y)
	level[currentlevel].setMapIdx(idx,1)
	delay(1)
	gg	= int(rnd()*500/currentlevel+1)
	if (player.gold - gg < 0):
		gg	= player.gold
	y	= int(rnd()*8+1)
	if (y <= 3):
		print(" ")
		print("You surprised the thief. . . . ")
		delay(1)
		print("As he runs out, he drops . . . . ")
		gg	= int(rnd()*400/currentlevel+1)
		print(f". . . {gg} gold pieces")
		player.gold = player.gold + gg
		print("")
	else:
		print(" ")
		print(". . . . . . He surprises you")
		delay(1)
		print("As he quickly passes by you, he")
		print(f"snatches. . . {gg} gold pieces.")
		player.gold = player.gold - gg
	if player.hasmap:
		return
	else:
		ma = int(rnd()*4+1)
		if (ma <= 2):
			getMap()
	return
	
def playerDead():
	global player
	global newgame
	
	delay(2)
	cls()
	if player.movesdepleted:
		print(f"{player.name}, you have run out of moves.")
	else:
		print("Your hit-points are depleted.")
	player.gold = 0
	print("And, unfortunately, you have died.")
	delay(2)
	w	= int(rnd()*6+1)
	player.dead	= False
	if (player.movesdepleted == False) and (w >= 3):
		delay(1)
		player.hp	= player.initialhp
		flourish()
		print("")
		print("You have entered .. a zone")
		print("between .. Life and Death")
		print(" ")
		delay(1)
		print("I.... The Ancient Wizard")
		print(f"will restore your hit-points to {player.initialhp}")
		print("and .... You have one more")
		print("chance in the Dungeon.")
		print(" ")
		player.turnsleft = int(rnd()*15+1)*player.monsterskilled+10
		print(f'You shall have {player.turnsleft} moves')
		print("left to find your way out")
		print("of the Dungeon of Danger.")
		delay(2)
		flourish()
	else:		# Kube 1710 (that's what happens when you type with your hands shifted one key to the left
		print("You lost all your gold and you were")
		print("... unable to meet the demands of")
		print(".....The Dungeon of Danger")
		print("\n\n")
		print(" ")
		print("Better luck next time")
		gg=player.gold + 100
		r = int ((gg*player.monsterskilled-7000+1)/player.turnstaken)
		rating = getRating(r)
		print(f'Game rating is {r} = {rating}')
		print(" ")
		print("Another game?")
#		f=input("Enter (Y)es or (N)o >")
		f	= yesNo()
		if f == 'Y':
			newgame = True	# Goto 210
			cls()
		else:
			quit()
	return
		
def deadMonster():
	global player
	
	delay(1)
	print("")
	print(f"You have killed the {monster.name}")
	print("")
	if (inroom < 6) and (inroom !=2):
		level[currentlevel].setMapIdx(index,1)
	gold	= 500
	givegold	= int(rnd()*gold/currentlevel+1)+75
	if (inroom >= 6):
		gold = 250
	elif (inroom == 2):
		givegold=givegold*2
	player.gold = player.gold+givegold
	delay(2)
	print("You search the area. . . . ")
	delay(1)
	print(f"and find ... {givegold} gold pieces")
	player.monsterskilled = player.monsterskilled + 1
	player.totalkills = player.totalkills + 1
	if player.haskey != True:
		checkKey()
	return
	
def monsterAttacks():
	global player
	global monster
	
	print("")
	w	= int(rnd()*7+1)
	print(". . . . . . . It attacks you")
	if (w <= 2):
		print("But. . . . . . It misses")
		delay(1)
	else:
		w = int(rnd()*6+1)
		if (w >= 3):
			n	= int(rnd()*player.hp*difficulty+1)
		else:
			n	= int(rnd()*player.hp/currentlevel+1)+int(rnd()*player.hp/currentlevel+1)
		if monster.hm <= 2:
			n = 1
		player.decHP(n)
		delay(1)
		print(f"And it does {n} hit-points of damage")
		print(" ")
		print(f"You have . . . {player.hp} hit-points left")
		print(" ")
	return
	
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

def yesNo():
	print("")
	f = input("Enter (Y)es or (N)o > ")
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
	
	if player.hasMoved() == False:
		print("You are in a misty cavern.")
		return
		
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
		dl	= int(rnd()*6+1)
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
				print(f"Which decreased your hit-points by {h}.")
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
	if (w == 1) and (player.hp < player.initialhp):
		mrWizard()
	elif (w == 2):
		giantSpider()
	elif (w == 4) and (currentlevel > 1):
		fallInPool()
	else:
		darkWizard()
	return

def introTop():
	cls()
	showFile("./intro.txt")
	delay(5)
	delay(2)
	print("\n")
	print("The Dungeon of Dangeresque".center(40))
	print("   For Python 3".center(40))
	print("(c) 1980 by Howard Berenbon".center(40))
	print("Adapted from Atari BASIC verson".center(40))
	print("Of 'Dunger of Danger'".center(40))
	print(" ")
	print("A Fantasy Game".center(40))
	print("=-=-=-=-=-=-=-=-=-=-".center(40))
	print("You will be teleported to...")
	print(" ")
	return

def introMiddle():
	print("The...")
	showFile("./DungeonOfDangeresque-Logo.txt")
	print(" ")
	return

def introBottom():
	print(f'You carry a magic sword and {player.gold} gold pieces with you.')
	print(f'Your hit-point value is {player.hp}.')
	print("If it reaches zero, you will die . . . So be careful!")
	delay(1)
	print(f'{player.name} . . . You are on your way.')
	delay(3)
#	cls()
	print("\n\n\n")
	print("You have arrived at . . . ")
	print(f"The Dungeon of Danger . . . Level {currentlevel}")
	print(" ")
	print("You will encounter monsters and thieves and . . . gold.")
	print("Good luck!")
	delay(3)
	return

def showCommands():
	if debug:
		print(f"Player X = {player.x}   Player Y = {player.y}  Room Type = {inroom} Level = {currentlevel}")
		print(f"Monsters Killed (level)= {player.monsterskilled}  Monsters Killed (total) = {player.totalkills}")
		print(f"Has Key = {player.haskey}  Has Map = {player.hasmap}")
		print("\n")
	print(f'Hit Points: {player.hp}  Gold: {player.gold}')
	print(f'{player.name}, what is your action or move?')
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap")
	if debug:
		print("($)Give map & Key  (1) Show raw level")
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
#			level[i].map	= fillMap()
			fillMap(i)
		
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
		player.initialhp		= 20+int(rnd()*15+1)
		player.initialhp		= player.initialhp//difficulty
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
	elif (inroom == 3 ) or (inroom == 4):
		occupiedCavern()
	elif (inroom == 5):
		thief()
	elif (inroom == 6):
		nsCorridor()
	elif (inroom == 7):
		ewCorridor()
	elif (inroom == 8):
		trapDoor()
	elif (inroom == 9):
		print("You are at a stairway")
		print(". . . . . . .going up")
	print(" ")
	if player.dead:
		playerDead()
		continue
		
	showCommands()
	pmove	= input("==> ")
	pmove	= pmove.upper()
		
	if (pmove == 'N'):
		if (player.y - 1 == 0):
			atWall("North")
		elif (inroom == 7):
			print("You are in an East-West passage.")
		else:
			player.move(player.x,player.y-1)
	elif (pmove == 'E'):
		if (player.x + 1) == 9:
			atWall("East")
		elif (inroom == 6):
			print("You are in a North-South passage.")
		else:
			player.move(player.x+1,player.y)
	elif (pmove == 'S'):
		if (player.y + 1 == 9):
			atWall("South")
		elif (inroom ==7):
			print("You are in an East-West passage.")
		else:
			player.move(player.x,player.y+1)
	elif (pmove == 'W'):
		if (player.x - 1 == 0):
			atWall("West")
		elif (inroom == 6):
			print("You are in a North-South passage.")
		else:
			player.move(player.x-1,player.y)
		
	elif (pmove == 'U'):
		goUpstairs()
	elif (pmove == 'M'):
		showMap()
	elif (pmove == 'Q'):
		quit()
	print(" ")
	inroom = level[currentlevel].roomContents(player.x,player.y)
	player.turnEnd()
	delay(2)
		
