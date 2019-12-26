from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import sleep
import keyboard
from pygame import mixer

mc = Minecraft.create()
pos = mc.player.getPos()
playerSprite = block.Block(35,14)
Tv_is_built = False
leaveGame = False
def buildTv():
	blackWool = block.Block(35,15) 
	mc.setBlocks(pos.x,pos.y,pos.z + 20,pos.x,pos.y + 10,pos.z + 20,blackWool)
	mc.setBlocks(pos.x,pos.y,pos.z + 20,pos.x + 20,pos.y,pos.z + 20,blackWool)
	mc.setBlocks(pos.x + 20,pos.y,pos.z + 20,pos.x + 20,pos.y + 10,pos.z + 20,blackWool)
	mc.setBlocks(pos.x,pos.y + 10,pos.z + 20,pos.x + 20,pos.y + 10,pos.z + 20,blackWool)
def play():
	global mc
	global pos
	global playerSprite
	global Tv_is_built
	global leaveGame

	gameStart = False
	fromIndex = 0
	toIndex = 19
	playerX = 1
	playerY = 5
	timesToUp = 0
	mixer.init()
	mixer.music.load('Music\Super-Mario-Bros.mp3')
	while(True):
		if(keyboard.is_pressed('M')):
			if(Tv_is_built == False):
				buildTv()
				Tv_is_built = True
				mixer.music.load('Music\Super-Mario-Bros.mp3')
				mixer.music.play()
				gameStart = True
				mc.postToChat('Game started. To end the game, press L')
				break
			if(Tv_is_built == True) and ((mc.player.getPos().x > pos.x + 10 or mc.player.getPos().z > pos.z + 10 or mc.player.getPos().y > pos.y + 10) or (mc.player.getPos().x < pos.x + 10 or mc.player.getPos().z < pos.z + 10 or mc.player.getPos().y < pos.y + 10)):
				mc.setBlocks(pos.x + 20,pos.y,pos.z + 20,pos.x,pos.y + 10,pos.z + 20,0)
				pos = mc.player.getPos()
				buildTv()
				mixer.music.load('Music\Super-Mario-Bros.mp3')
				mixer.music.play()
				gameStart = True
				mc.postToChat('Game started. To end the game, press L')
				break
			else:
				mixer.music.load('Music\Super-Mario-Bros.mp3')
				mixer.music.play()
				gameStart = True
				mc.postToChat('Game started. To end the game, press L')
				break

	#blocks

	g = 2 #Grass
	d = 3 #Dirt
	a = 79 #Sky
	b = 45 #Bricks
	l = 19 #Lucky block
	p = 133 #Pipe
	k = 49 #Black
	w = 35 #White

	destroyedBlocks = []

	#Main game loop
	while(gameStart == True):

	    map = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
	           [a,a,a,a,a,a,a,a,a,a,a,l,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,a,a,a,a],
	           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,b,b,b,a,a,a,b,b,b,l,a,a,a,a,a,a,a,a,a,a,a,a,l,a,a,a,a,a,a,a,a,b,b,b,a,a,a,a,b,l,l,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,b,a,a,a,a,a,a,a,a,a,a,b,k,b,a,a,a],
	           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,p,p,p,p,a,a,a,a,a,a,p,p,p,p,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,a,a,b,a,a,a,a,a,a,a,a,a,a,a,a,b,b,a,a,b,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,l,b,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,b,b,a,a,a,a,a,a,a,b,a,b,b,b,b,b,a,b],
	           [a,a,a,a,a,a,l,a,a,b,l,b,l,b,a,a,a,a,a,a,a,a,a,a,p,p,p,p,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,l,b,a,a,a,a,a,a,a,a,a,a,a,a,a,b,a,a,a,a,b,b,a,a,a,a,l,a,l,a,l,a,a,a,a,b,a,a,a,a,a,a,a,a,a,b,b,a,a,a,a,a,b,b,a,a,b,b,a,a,a,a,a,a,a,a,a,a,b,b,b,a,a,b,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,b,b,b,b,b,b],
	           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,p,p,p,p,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,a,a,b,b,b,a,a,a,a,a,a,a,a,b,b,b,b,a,a,b,b,b,a,a,a,a,p,p,p,p,a,a,a,a,a,a,a,a,a,a,a,a,p,p,p,p,a,b,b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,k,k,k,b,b,b],
	           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,p,p,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,b,b,b,a,a,b,b,b,b,a,a,a,a,a,a,b,b,b,b,b,a,a,b,b,b,b,a,a,a,a,p,p,a,a,a,a,a,a,a,a,a,a,a,a,a,a,p,p,a,b,b,b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,k,k,k,b,b,b],
	           [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
	           [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]
	          ]

	    currentPos = mc.player.getPos()
	    currentPos.x = pos.x + 10
	    currentPos.y = pos.y
	    currentPos.z = pos.z + 5

	    fromX = pos.x + 19
	    fromY = pos.y + 1
	    fromZ = pos.z + 20

	    toX = pos.x + 1
	    toY = pos.y + 9
	    toZ = pos.z + 20

	    #Clear
	    mc.setBlocks(fromX,fromY,fromZ,toX,toY,toZ,0)
	    #Deleting destroyed blocks from the map
	    for row in range(0,len(destroyedBlocks)):
	        if(destroyedBlocks[row][0] > 0):
	            map[destroyedBlocks[row][0]][destroyedBlocks[row][1]] = a
	    map[playerY][playerX] = playerSprite
	    #Build map
	    for row in map:
	        for block in row[fromIndex:toIndex]:
	            mc.setBlock(fromX,toY,fromZ,block)
	            fromX -= 1
	        toY -= 1
	        fromX = pos.x + 19
	    try:
	        #Move left
	        if (keyboard.is_pressed('Left')):
	            if (playerX != fromIndex) and (map[playerY][playerX - 1] == a):
	                playerX -= 1

	        #Move right
	        if (keyboard.is_pressed('Right')):
	            if (map[playerY][playerX + 1] == a):
	                playerX += 1
	                if(toIndex != len(map[0])) and (playerX == toIndex - 8):
	                    fromIndex += 1
	                    toIndex += 1
	    except:
	        pass
	    #Jump
	    if (keyboard.is_pressed('Up')):
	        if(map[playerY + 1][playerX] != a) and (playerY != 0):
	            timesToUp = 5
	    if(timesToUp > 0):
	        if(map[playerY - 1][playerX] == a) and (playerY != 0) and (playerY != len(map) - 1):
	            playerY -= 1
	            timesToUp -= 1
	        else:
	            if(map[playerY - 1][playerX] == l) or (map[playerY - 1][playerX] == b):
	                if(destroyedBlocks.count([playerY - 1,playerX]) == 0):
	                    destroyedBlocks.append([playerY - 1,playerX])
	            timesToUp = 0
	    if(playerY == 8):
	        mixer.music.load('Music\you-re-dead.mp3')
	        mixer.music.play()
	        sleep(6)
	        break
	    try:
	        if (timesToUp == 0) and (map[playerY + 1][playerX] == a):
	            playerY += 1
	    except:
	        playerY += 1
		#Pause
	    if(keyboard.is_pressed('P')):
	    	mc.postToChat('PAUSE. To continiue, press Q')
	    	while True:
	    		keyboard.wait('Q')  
	    		break
		#Leave game
	    if(keyboard.is_pressed('l')):
	    	leaveGame = True
	    	mc.setBlocks(pos.x + 20,pos.y,pos.z + 20,pos.x,pos.y + 10,pos.z + 20,0)
	    	break
	    if(playerX == len(map[0]) - 10):
		    mixer.music.load('Music\level-complete.mp3')
		    mixer.music.play()
		    sleep(8)
		    break
	    #sleep(0.07)
	mc.postToChat('GAME OVER!')

while True:
	play()
	if(leaveGame == True):
		break

