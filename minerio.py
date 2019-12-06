from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import sleep

mc = Minecraft.create()
pos = mc.player.getPos()
gameStart = False
fromIndex = 0
toIndex = 19
playerX = 1
playerY = 5
playerSprite = block.Block(35,14)
timesToUp = 0


#Build TV
blackWool = block.Block(35,15) 
mc.setBlocks(pos.x,pos.y,pos.z + 20,pos.x,pos.y + 10,pos.z + 20,blackWool)
mc.setBlocks(pos.x,pos.y,pos.z + 20,pos.x + 20,pos.y,pos.z + 20,blackWool)
mc.setBlocks(pos.x + 20,pos.y,pos.z + 20,pos.x + 20,pos.y + 10,pos.z + 20,blackWool)
mc.setBlocks(pos.x,pos.y + 10,pos.z + 20,pos.x + 20,pos.y + 10,pos.z + 20,blackWool)
#Build buttons
mc.setBlock(pos.x + 10,pos.y - 1,pos.z + 5,block.Block(35,11))#Playground
mc.setBlock(pos.x + 9,pos.y - 1,pos.z + 5,block.Block(35,14))#Play
mc.setBlock(pos.x + 11,pos.y - 1,pos.z + 5,block.Block(35,5))#Reset


while(True):
    if(mc.getBlock(pos.x + 11,pos.y - 1,pos.z + 5) == 0):
        mc.postToChat('GAME OVER!')
        break
    if(mc.getBlock(pos.x + 9,pos.y - 1,pos.z + 5) == 0):
        gameStart = True
        mc.postToChat('GAME START!')
        break
#Blocks

g = 2 #Grass
d = 3 #Dirt
a = 79 #Sky

#Main game loop
while(gameStart == True):

    map = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
           [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,g,g,g,g,g,g,g,g,g,g],
           [a,a,a,a,a,a,a,a,a,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,a,a,a,a,a,a,a,a,a,a,a],
           [g,a,a,a,a,a,a,a,g,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,g,a,a,a,a,a,a,a,a,a,a,a],
           [d,g,g,g,g,g,g,g,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,g,g,g,g,g,g,g,g,g,g,g],
           [d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d],
           [d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d]
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
    map[playerY][playerX] = playerSprite
    #Build map
    for row in map:
        for block in row[fromIndex:toIndex]:
            mc.setBlock(fromX,toY,fromZ,block)
            fromX -= 1
        toY -= 1
        fromX = pos.x + 19
    #Move left
    if (mc.player.getPos().x > currentPos.x):
        mc.player.setPos(currentPos.x,currentPos.y,currentPos.z)
        if (playerX != fromIndex) and (map[playerY][playerX - 1] == a):
            print('<')
            playerX -= 1
            if(fromIndex != 0):
                fromIndex -= 1
                toIndex -= 1


    #Move right
    if (mc.player.getPos().x < currentPos.x):
        mc.player.setPos(currentPos.x,currentPos.y,currentPos.z)
        if (map[playerY][playerX + 1] == a):
            print('>')
            playerX += 1
            if(toIndex != len(map[0]) - 1):
                fromIndex += 1
                toIndex += 1
    #Jump
    if(mc.player.getPos().y > currentPos.y):
        mc.player.setPos(currentPos.x,currentPos.y,currentPos.z)
        if(map[playerY + 1][playerX] != a) and (playerY != 0):
            timesToUp = 3
    if(timesToUp > 0):
        if(map[playerY - 1][playerX] == a):
            playerY -= 1
            timesToUp -= 1
            print(timesToUp)
        else:
            timesToUp = 0
    try:
        if (timesToUp == 0) and (map[playerY + 1][playerX] == a):
            playerY += 1
    except:
        playerY += 1
    #if(playerX > round(((toIndex - fromIndex) / 2))) and (toIndex != len(map) - 1):
        #toIndex += 1
        #fromIndex += 1

    #sleep(0.1)