####           The Dungeon of Danger                   ####   
####        (c) 1980 by Howard Berenbon                ####
#### Transcribed from:                                 ####
#### Mostly BASIC: Applications for your Atari, Book 2 ####
#### Published by Howard W. Sams & Co., Inc            ####
#### Indianapolis, Indiana 1983                        ####
####             Python Version 1.00                   ####

## Imports ##
from random import random
#from tools import getIndex, createGrid, showGrid
from os import system, name
from time import sleep
from dodfun import cls, rnd, delay, playerObject, monsterObject, levelObject

## Functions ##
def getDifficulty():			#Line 5530
	difficulty	= 0
	while (difficulty < 1) or (difficulty > 2):
		print("Difficulty Level: 1 = Moderate, 2 = Hard")
		n = input("Enter difficulty level > ")
		difficulty = int(n)
	return(n)

def getLevels():
	global
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
	
def getRating(r):
	if r <= -400:
		retrate = "Incompetent serf"
	elif r <= -100:
		retrate = "Weakling"
	elif r < 0:
		retrate = "Apprentice"
	elif r < 100:
		retrate = "Halfling"
	elif r < 200:
		retrate = "Foot soldier"
	elif r < 600:
		retrate = "Warrior"
	elif r < 900:
		retrate = "Great warrior"
	elif r < 1500:
		retrate = "Swordsman"
	elif r < 2500:
		retrate = "Magic Swordsman"
	elif r >= 2500:
		retrate = "Dungeon Master!"
	return(retrate)

def gameWon():		# Line 890
	print("You found your way...")
	print("... Out of the Dungeon of Danger")
	print(" ")
	print(f'You have acquired {player.gold} gold pieces.')
	gg=player.gold + 100
	r = int ((gg*player.monsterskilled-7000+1)/player.turnstaken)
	rating = getRating(r)
	print(f'Game rating is {r} = {rating}')
	if (player.gold <= 0):
		print(f'You killed {player.monsterskilled} monsters ')
		print(f'..... in {player.turnstaken} turns.')
	else:
		print(f'You took {player.turnstaken} turns to find the way out')
		print(f'And killed {player.monsterskilled} monsters.')
	quit()
	return

def flourish():				# This needs to be re-done
	for aa in range(1,301):
		print("*        %",end="")
	delay(2)
	print("\n")
	cls()
	return

def showMap():		# Line 1570 & 1990
	cls()
	if (player.hasmap == False):
		print("You don't have the map.")
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
					idx = getIndex(n,q,9)
					s1	= level[currentlevel].map[idx]
					if s1 == 1:
#						pass()		# Line 2910
						print("O  ",end=" ")
					elif s1 == 2:
#						pass()		# Line 2970
						print("C  ",end=" ")
					elif s1 == 3:
#						pass()		# Line 2930
						print("M  ",end=" ")
					elif s1 == 4:
#						pass()		# Line 2930
						print("M  ",end=" ")
					elif s1 == 5:
#						pass()		# Line 2950
						print("?  ",end=" ")
					elif s1 == 6:
#						pass()		# Line 2990
						print("NS ",end=" ")
					elif s1 == 7:
#						pass()		# Line 3010
						print("EW ",end=" ")
					elif s1 == 8:
#						pass()		# Line 3030
						print("?  ",end=" ")
					elif s1 == 9:
#						pass()		# Line 3040
						print("UP ",end=" ")
			print("\n")
	dummy = input("~~Press Enter to Continue~~")
	return

def getMap():
	print("You search the chamber and")
	delay(1)
	print("You. . . . . find a map")
	return

def getKey():		# Line 3110
	global player
	
	player.haskey = True
	print("\nYou look to the ground......")
	print("and find the Enchanted Key!")
	delay(2)
	return

def checkKey():		# Line 3190
	if player.monsterskilled >= targetKills:
		getKey()	# GOTO 3110
	return

def playerDead():
	global dy
	global player
	global newgame
	
	delay(2)
	cls()
	if player.movesdepleted:
		print(f'{player.name}, you have depleted your moves.')
	else:
		print("Your hit-points have been depleted,")
	player.gold = 0
	print("And unfortunately... You just died.")
	delay(3)
	w = int(rnd()*6+1)
	player.dead = False
	if (player.movesdepleted == False) and (w >= 3):	# Line 5370
		delay(1)
		dy = 1
		player.hp = initialHP
		flourish()
		print("",end='\n')
		print("You have entered .. a zone")
		print("between .. Life and Death")
		print(" ")
		delay(1)
		print("I.... The Ancient Wizard")
		print("will restore your hit-pointes to "+str(initialHP))
		print("and .... You have one more")
		print("chance in the Dungeon.")
		print(" ")
		player.turnsleft = int(rnd()*15+1)*player.monsterskilled+10
		print(f'You shall have {player.turnsleft} moves')
		print("left to find your way out")
		print("of the Dungeon of Danger.")
		delay(2)
		flourish()
	else:		# Kube 1710
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
		f=input("Enter (Y)es or (N)o >")
		if f.upper() == 'Y':
			newgame = True	# Goto 210
			cls()
		else:
			quit()
	return


def deadMonster():	# Line 4890
	global player
	
	delay(2)
	print("")
	print(f'You have killed the {monster.name}')
	print("\n")
	if (inroom < 6) and (inroom != 2):
		level[currentlevel].setMapIdx(index,1)
	gold = 500
	if inroom >= 6:
		gold = 250
	givegold = int(rnd()*gold/currentlevel+1)+75
	if inroom == 2:
		givegold=givegold*2
	player.gold = player.gold+givegold
	delay(2)
	print("You search the area....")
	delay(2)
	print(f'and find ... {givegold} gold pieces')
	player.monsterskilled = player.monsterskilled + 1
	if player.haskey != True:
		if level == 1:
			checkKey()	# GOTO 3190
		else:
			getKey()	# GOTO 3110
	return	

def monsterAttacks():	# Line 4780
	global player
	global monster
	
	print(" ")
	w = int(rnd()*7+1)
	print(". . . . . . . It attacks you")
	if (w <= 2):
		print("But . . . . . . . .  it misses")
		delay(2)
	else:
		w = int(rnd()*6+1)
		if (w >= 3):
			n = int(rnd()*player.hp*difficulty+1)
		else:
			n = int(rnd()*player.hp/currentlevel+1)+int(rnd()*player.hp/currentlevel+1)
		if monster.hm <= 2:
			n = 1
		player.decHP(n)
		delay(1)
		if player.dead:
			return
		print(f'And it does {n} hit points of damage')
		print(" ")
		print(f'You have . . . {player.hp} hit points left')
		print(" ")
	return

def attackMonster():	# Line 4600
	global monster
	
	cls()
	delay(1)
	print(f'You attack the . . . {monster.name}')
	delay(1)
	print("With a swing of your sword")
	n = int(rnd()*5+1)+int(rnd()*player.monsterskilled/2+1)
	monster.hm = monster.hm - n
	if monster.hm <= 0:
		deadMonster()	# GOTO 4890
		return(monster.hm)
	print(f'You do {n} hit points of damage')
	delay(1)
	print(f'It has . . {monster.hm} hit points left')
	delay(1)
	return(monster.hm)
	
def flee():		# Line 4700
	global player
	
	w = int(rnd()*4+1)
	player.x = player.oldx
	player.y = player.oldy
	print("You quickly run out . . .")
	if tl == 1:
		teleportTrap()	# GOTO 5560
	n = int(rnd()*2+1)
	delay(2)
	if w >= 3:
		pass	# GOTO 5330
		player.decHP(n)
		print(f'As you leave . . . ')
		print(f'the {monster.name} attacks')
		delay(1)
		if player.dead:
			return
		print(f'And it does {n} hit points of damage')
		delay(2)
	return
	
def fightOrFlee():
	print(" ")
	f = input("Will you (F)ight or (R)un? ")
	return(f)
		
def doBattle():
	battleloop = True
	delay(2)
	print(" ")
	w = int(rnd()*4+1)
	if (w > 2):
		delay(1)
		monsterAttacks()	# GOSUB 4780
		if player.dead:
			battleloop = False
			return
	while battleloop:
		f = fightOrFlee()
		if f.upper() == 'F':
			check = attackMonster()
			if check <= 0:
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

def atWall(dir):
	print(f'You are at the {dir} wall')
	print("You cannot pass through")
	print(" ")
	print("Try another direction?")
	return
	
def emptyChamber():		# Line 2100
	w=int(rnd()*2+1)
	if w == 2:			# THEN 2160
		print("You are in a damp and misty")
		print("...... Empty chamber.")
		print("")
	else:
		print("You are in a cold and dark")
		print("...... Empty chamber.")
		print("")
	return

def nsCorridorMsg():	# Line 1660
	cls()
	print("You are in a North-South corridor")
	print("You can only go North or South.")
	return

def ewCorridorMsg():	# Line 1620
	cls()
	print("You are in an East-West corridor")
	print("You can only go East or West")
	return

def intoPit():		# Not 100% sure this is all correct
	global pitfall
	global player
	
	print("You fell into a deep . . . pit")
	pitfall = True
	delay(1)
	print("Luckily . . you didn't get hurt")
	print(" ")
	delay(1)
	print("But in climbing out . . . ")
	player.gold = 0
	print("\nYou . . . . . . lost")
	print("all of your gold pieces")
	print(" ")
	if pitfall:
		pitfall = False
		return
	if player.haskey:
		print("But . . . you still have your key")
	return
	
def trapDoor():		# Line 2610		Not sure this is right, either
	global currentlevel
	global player
	
	print("You activated a . . . trap door")
	delay(2)
	trap = int(rnd()*4+1)*difficulty
	if trap > 4:
		print("You fell thru . . . ")
		delay(2)
		pass		# GOTO 1720
		player.dead = True
		return
	elif trap == 4:
		pass		# GOTO 2690
		if currentlevel > 1:
			pass	# GOTO 2800
			intoPit()
			return
		currentlevel = currentlevel + 1
		print(" ")
		player.haskey = True
		print(f"You fell thru to level {currentlevel} . . . and")
		delay(1)
		intoPit()
		return
	else:
		print("But . . . you caught yourself")
		print("from falling")
		return
	return

def goUpstairs():	# Line 1480
	global currentlevel	# should put level in playerObject
	global player
	
	cls()
	if (inroom != 9):
		print("You are not at a stairway.")
		delay(1)
	else:
		if player.haskey:
			currentlevel = currentlevel -1
			print("You walk up the stairway...")
			delay(1)
			print("The Enchanted Key ... Opens the lock")
			delay(1)
			if currentlevel  == 0:
				gameWon()
			else:
				player.hasmap = False
				player.haskey = False
				k4 = int(rnd()*4+1)+1
				if player.hp < initialHP:
					player.hp = initialHP
					print("You feel stronger .....")
					delay(1)
					print(f'Your hit points are restored to {initialHP}')
					print(" ")
					bmonsterskilled = player.monsterskilled+k4
					print("You are at..... Level 1")
					delay(2)
					return
		else:
			print("\nYou cannot go up the stairway.")
			print("You don't have the key.")
			delay(1)
	return

def corridor():		# Line 3240
	global monster
	
	print("The door closes and locks behind you")
	delay(1)
	w = int(rnd()*8+1)
	if w >= 7:
		# GOTO 3300
		w = int(rnd()*4+1)+30
		monster.name	= monsterInfo[0][w]
		monster.hp		= monsterInfo[1][w]
		monster.hm		= monsterInfo[2][w]
		print("There is something lurking")
		print("In this corridor . . . ")
		delay(1)
		print(". . . . Beware")
		delay(1)
		print(f"\nIt is a . . . . . {monster.name} . . ")
		delay(1)
		doBattle()
		return
	w = int(rnd()*8+1)
	if w == 8:
		# GOTO 3390
		if player.haskey == False:
			player.haskey = True
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
		player.oldx = player.x
		player.oldy = player.y
		print("Suddenly you feel dizzy, and pass out")
		delay(2)
		flourish()
		print("When you wake up . . . you find")
		print("that you were . . . . teleported")
		print("to an unknown location . . . . ")
		delay(2)
	return
	
def nsCorridor():	# Line 1660
	cls()
	print("You are in a North-South corridor")
	print("You can only go North or South.")
	corridor()
	return

def ewCorridor():	# Line 1620
	cls()
	print("You are in an East-West corridor")
	print("You can only go East or West")
	corridor()
	return
	
def findVial():	# Line 4210
	global player
	
	print("\nYou look around...")
	delay(2)
	v=int(rnd()*7+1)
	if v < 5:
		return
	print("On the ground, at your feet, is a vial.")
	delay(2)
	print("You pick up the vial.. and see that")
	print("It contains ... a milky liquid.")
	print("Would you like a drink?")
	d=input("Enter (Y)es or (N)o:")
	dl=int(rnd()*6+1)
	if d.upper() == 'N':
		return
	print("\nYou take a drink...")
	delay(3)
	cls()
	if dl >= 3:
		h=int(rnd()*10/difficulty+1)+(6/difficulty)
		player.incHP(h)
		print("It was a white magic potion...")
		print(f'Which increased your hit-points by {h}')
	elif dl == 2:
		print("The liquid had no effect on you.")
	else:
		h=int(rnd()*6+1)*difficulty
		player.decHP(h)
		print("You feel a little funny...")
		delay(4)
		if player.dead:
			return
		print("\nIt was a black magic potion...")
		print(f'Which decreased your hit-points by {h}.')
	return

def somethingJumps():	# Line 5290
	cls()
	print("Suddenly... something jumps...")
	print("in front of you......")
	delay(2)
	cls()
	return

def thief():
	global player
	global level
	
	cls()
	print("There is a thief in this chamber")
	idx=level[currentlevel].getIndex(player.x,player.y)
	level[currentlevel].setMapIdx(idx,1)
	delay(1)
	g4 = int(rnd()*500/currentlevel+1)
	if (player.gold - g4 < 0):
		g4 = player.gold
	y = int(rnd()*8+1)
	if y <= 3:
		print(" ")
		print("You suprised the thief . . . . ")
		delay(1)
		print("As he runs out, he drops . . . . ")
		g4 = int(rnd()*400/currentlevel+1)
		print(f'. . . {g4} gold pieces.')
		print("You pick up the gold pieces")
		player.gold = player.gold + g4
		print(" ")
		if player.hasmap:
			return
		ma = int(rnd()*4+1)
		if ma <= 2:
			player.hasmap = True
			getMap()
		return
	else:
		print("\n. . . . . . . . He surprises you")
		delay(2)
		print("As he quickly passes by you, he")
		print(f'snatches . . . {g4} gold pieces.\n')
		player.gold = player.gold - g4
		if player.hasmap:
			return
		else:
			ma = int(rnd()*4+1)
			if ma <= 2:
				player.hasmap = True
				getMap()
	return

def fallInPool():	# Have not seen if this works yet
	global monster
	
	cls()
	print("You fall into a deep . . dark")
	delay(1)
	print(". . . pool . . of murky water")
	delay(3)
	w = int(rnd()*6+1)
	print(" ")
	if (w >= 5):
		# GOTO 5780
		monster.name = 'Gill Monster'
		monster.hp	= 8
		monster.hm	= 14
		cls()
		print("The water is . . . icy cold")
		delay(4)
		print("Suddenly . . you feel something warm")
		print(" . . . Rub against your legs . . . .")
		delay(3)
		print(" ")
		print("It then surfaces next to you . . . ")
		print(" and you see that is is a slimy . . ")
		print(f'. . . {monster.name} . . ready to attack')
		delay(2)
		print()
		print("As you climb out . . . ")
		delay(2)
		doBattle()
		return
	elif (w >= 3):
		# GOTO 5860
		print("The water is steaming . . . . hot")
		delay(3)
		print()
		print("As you quickly jump out . . . . ")
		g4 = int(rnd()*500+1)+100
		if (player.gold - g4) < 0:
			g4 = player.gold
		player.gold = player.gold - g4
		print(f'You drop {g4} gold pieces')
		print("Which fall into the pool . . lost")
		delay(3)
	else:
		print("It is warm and soothing . . And")
		delay(2)
		print("You climb out . . feeling relaxed")
		print(" ")
	return
	
def giantSpider():	# Line 5170
	global monster
	
	monster.name = "Giant Spider"
	monster.hp = 6
	monster.hm = 12
	print("It's a huge man-sized crawling")
	print("....... SPIDER .......")
	delay(2)
	print("...... and ......")
	doBattle()		# GOTO 4530
	return

def mrWizard():	# Line 5040
	global player
	
	print("Halt... I am the Ancient Wizard")
	print("I will not harm you......")
	delay(4)
	print(" ")
	gold=int(rnd()*300+1)+100
	player.gold = player.gold + gold
	print(" ")
	print(f'I give you... {gold} gold pieces')
	print("Out of good will and friendship.")
	print(" ")
	hp = int(rnd()*10/difficulty+1)+(6/difficulty)
	player.incHP(hp)
	print("Also, I will increase...")
	print(f'your hit-points by {hp}.')
	delay(2)
	return

def darkWizard():	# Line 5230
	global monster
	
	monster.name	= 'Dark Wizard'
	monster.hp		= 8
	monster.hm		= 14
	cls()
	print(f"Do not pass . . . I am the {monster.name}")
	delay(2)
	print("And I will hack you to pieces . . . ")
	delay(2)
	doBattle()
	return
	
def occupiedCavern():
	if inroom == 4:
		w = int(rnd()*15+1)+15
	else:
		w = int(rnd()*15+1)
		
	print(" ")
	print("There is something lurking...")
	print(".... in this chamber ....")
	delay(1)
	print("........... Beware")
	delay(1)
	print(" ")
	monster.name = monsterInfo[0][w]
	monster.hp   = monsterInfo[1][w]
	monster.hm   = monsterInfo[2][w]
	print(f'It is a ..... {monster.name} .. ')
	delay(2)
	# continue at 4510
	doBattle()
	return
	
def hiddenCavern():	# Line 4060
	print("You stumbled onto .....")
	print("A hidden cavern")
	delay(2)
	print(" ")
	findVial()		# GOSUB 4210
	if player.dead:
		playerDead()
	w=int(rnd()*9+1)
	delay(3)
	if w > 3:
		print("The cavern seems empty...")
		return
	delay(2)
	print("But wait... Before you proceed")
	delay(2)
	print(" ")
	print("You hear a noise off in the distance")
	delay(2)
	print("Cautiously, you walk towards the sound.")
	delay(2)
	w=int(rnd()*4+1)	# Line 4160
	if initialHP < player.hp:
		if w == 2:	# GOTO 5170
			somethingJumps()
			giantSpider()
	else:
		if w == 1:	# GOTO 5040
			somethingJumps()
			mrWizard()
		elif (w == 4) and level == 2:	
			fallInPool()				# GOTO 5720
		else:
			somethingJumps()
			darkWizard()				# GOTO 5230
	return
	
def introTop():
	cls()
	print("The Dungeon of Danger".center(40))
	print("   For Python 3".center(40))
	print("(c) 1980 by Howard Berenbon".center(40))
	print("Adapted from Atari BASIC verson".center(40))
	print(" ")
	print("A Fantasy Game".center(40))
	print("=-=-=-=-=-=-=-=-=-=-".center(40))
	print("You will be teleported to...")
	print(" ")
	return

def introMiddle():
	print("The Dungeon of Danger")
	print(" ")
	return

def introBottom():
	print(f'You carry a magic sword and {player.gold} gold pieces with you.')
	print(f'Your hit-point value is {player.hp}.')
	print("If it reaches zero, you will die . . . So be careful!")
	delay(1)
	print(f'{player.name} . . . You are on your way.')
	delay(3)
	cls()
	print("You have arrived at . . . ")
	print("The Dungeon of Danger . . . Level 2")
	print(" ")
	print("You will encounter monsters and thieves and . . . gold.")
	print("Good luck!")
	return

def showCommands():
	print(f"Player X = {player.x}   Player Y = {player.y}  Room Type = {inroom}")
	print(f'Hit Points: {player.hp}  Gold: {player.gold}')
	print(f'{player.name}, what is your action or move?')
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap")
	return

def showLevels():
#	print(level1)
	showGrid(level1,9)
	print("------------------------------")
#	print(level2)
	showGrid(level2,9)
	print("------------------------------")
	bummer=input("Press ENTER")
	return
	
## Known Variables ##
level	= [1]
player	= playerObject
monster = monsterObject
level.append(levelObject())
level.append(levelObject())

debug	= False

difficulty	= 1
maxlevels	= 2

pitfall		= True
newgame		= True
onload		= True
gameloop	= True

## Unknown Variables ##
tl	= 0
cb	= 0	## Random monster amount to get key?
md	= 0
te	= 1
dy	= 1
f	= ' '

#### Main Game Loop ####
while gameloop:

	if (onload == True):	# Do stuff for the first (and only) time
		introTop()
		monsterInfo	= monsterSetup()
		onload		= False
		level[1].createMap()
		level[2].createMap()
	
	if (newgame == True):	# Do stuff needed for a new game
		introMiddle()
		level[1].fillMap()
		level[2].fillMap()
		player.x				= int(rnd()*8+1)
		player.y				= int(rnd()*8+1)
		currentlevel			= 2
		index					= level[currentlevel].getIndex(player.x,player.y)
		level[2].setMap(player.x,player.y,1)
		player.movesdepleted	= False
		player.movesleft		= 100
		player.hasmap			= False
		player.haskey			= False
		player.gold				= 500
		difficulty				= int(getDifficulty())
		initialHP				= 20+int(rnd()*15+1)
		initialHP				= int(initialHP/difficulty)
		targetKills				= int(rnd()*4+1)+4
		player.name				= getName()
		player.hp				= initialHP
		delay(2)
		introBottom()
		inroom 					= level[currentlevel].roomContents(player.x,player.y)
		newgame					= False
	cls()
	
	if		inroom	== 1:
		emptyChamber()
	elif	inroom	== 2:
		hiddenCavern()
	elif	(inroom	== 3) or (inroom == 4):
		occupiedCavern()
	elif	inroom	== 5:
		thief()
	elif	inroom	== 6:
		nsCorridor()
	elif	inroom	== 7:
		ewCorridor()
	elif	inroom	== 8:
		trapDoor()			# GOTO 2610
	elif	inroom	== 9:
		print("You are at a stairway")
		print(". . . . . . going up")
	print(" ")
	if player.dead:
		playerDead()
		continue
	showCommands()
	pmove = input("==> ")
	
	if pmove.upper()	==	'N':
		if (player.y - 1 == 0):
			atWall("North")
		elif inroom == 7:
			ewCorridorMsg()
		else:
			player.move(player.x,player.y-1)

	elif pmove.upper()	== 'E':
		if (player.x  + 1) == 9:
			atWall("East")
		elif (inroom == 6):		# Why was this 9? That's a stair
			nsCorridorMsg()
		else:
			player.move(player.x+1,player.y)

	elif pmove.upper()	== 'S':
		if (player.y + 1) == 9:
			atWall("South")
		elif (inroom == 7):
			ewCorridorMsg()
		else:
			player.move(player.x,player.y+1)

	elif pmove.upper()	== 'W':
		if (player.x - 1) == 0:
			atWall("West")
		elif (inroom == 6):		# Originally 9 for some reason
			nsCorridorMsg()
		else:
			player.move(player.x-1,player.y)

	elif pmove.upper()	== 'U':
		goUpstairs()
	elif pmove.upper()	== 'M':
		showMap()
	elif pmove.upper()	== 'Q':
		quit()
	print(" ")
	inroom = level[currentlevel].roomContents(player.x,player.y)
	player.turnEnd()
	delay(3)
