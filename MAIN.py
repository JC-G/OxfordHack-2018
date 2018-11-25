import Map
import util3d
import Player
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random
import EmotionRecognitionMaster.real_time_video as rtv
import threading
#main loop
def startGame():

    main_loop = True
    util3d.initGLPG((800, 600))
    theta = 0
    game_state = "playing"  #menu, playing, gameover...
    our_player = Player.Player()
    theTerrain = Map.Terrain()
    clock = pygame.time.Clock()
    trees = []
    EMOTION = False

    class controlThread(threading.Thread):
        def __init__(self,name,counter):
            threading.Thread.__init__(self)
            self.threadID = counter
            self.name = name
            self.counter = counter
        def run(self):
            rtv.captureFrame()

    theThread = controlThread("a",1)
    theThread.start()
    for x in range(10):
        trees.append(util3d.Sprite3d("tree.png",0.03*random.randint(0,100)-.5,0,0.03*random.randint(0,100)-.5,.1))
    playerTree = util3d.Sprite3d("tree.png",0,0,0,.05)

    while main_loop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_loop = False

        #switch depending on game state
        if game_state == "playing":
            theVal = rtv.value
            collData = theTerrain.pixelData[int((1+our_player.position[0])*512)][int((1+our_player.position[1])*512)]
            if collData == 0:
                print("LOL UR SHIT")
            turnMagnitude = 0
            forwards = 0
            if EMOTION:
                turnMagnitude = theVal[1]*0.3
                if theVal[0] == 1:
                    forwards = -1
                if theVal[0] ==0:
                    forwards = 0
                if theVal[0] == -1:
                    forwards = 3

            else:

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:

                    forwards = -1
                if keys[pygame.K_s]:
                    forwards = 3
                if keys[pygame.K_a]:

                    turnMagnitude = -1
                if keys[pygame.K_d]:
                    turnMagnitude = 1

            #print(keys , turnMagnitude)
            our_player.move(turnMagnitude*0.01,forwards*0.01)
            glClearColor(0.5, 0.5, 0.5, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            util3d.enablePerspective()

            glLoadIdentity()

            gluLookAt(our_player.position[0]+math.cos(our_player.theta)/10, .05, our_player.position[1]+math.sin(our_player.theta)/10, our_player.position[0]-math.cos(our_player.theta)/30, 0, our_player.position[1]-math.sin(our_player.theta)/30, 0, 1,0)
            #glRotate(theta,0,1,0)
            theta+=0.03
            util3d.drawTerrain(theTerrain)
            for t in trees:
                util3d.renderSprite(t)
            playerTree.setPos(our_player.position[0],0,our_player.position[1])
            util3d.renderSprite(playerTree)
            pygame.display.flip()





            #handle playing input
            #draw game



    rtv.go = False
    theThread.join()
    pygame.quit()


if __name__ == "__main__":
    startGame()

