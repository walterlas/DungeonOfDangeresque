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
		
