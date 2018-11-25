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
import json
score  =0

#main loop
def push_score(result):

    data = {}
    data["players"]=[]
    data["players"].append({"name":result[0],"score":result[1]})
    with open('highscores.txt', 'w') as out:
        json.dump(data, out)
        
def startGame():
    global score
    main_loop = True
    util3d.initGLPG(util3d.scsz)
    theta = 0
    game_state = "playing"  #menu, playing, gameover...
    our_player = Player.Player()
    theTerrain = Map.Terrain()
    print(theTerrain.nodes)
    our_player.position = (theTerrain.nodes[0][0],theTerrain.nodes[0][1])
    our_player.theta = math.atan2(-theTerrain.nodes[1][1]+theTerrain.nodes[0][1],-theTerrain.nodes[1][0]+theTerrain.nodes[0][0])
    clock = pygame.time.Clock()
    EMOTION = False
    theFaces = util3d.FaceDisplay()
    theCar = util3d.Car()
    pygame.mixer.music.load("dubstep.wav")
    pygame.mixer.music.play(-1)

    goodSound = pygame.mixer.Sound("collect.wav")
    badSound = pygame.mixer.Sound("wrong.wav")
    offSound = pygame.mixer.Sound("wilhelm.wav")
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
    c = 1
    #for x in theTerrain.nodes:

        #trees.append(util3d.Sprite3d("tree.png",x[0]*c,0,-x[1]*c,.1))
    playerTree = util3d.Sprite3d("tree.png",0,0,0,.05)

    while main_loop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_loop = False
                break

        #switch depending on game state
        if game_state == "playing":
            theVal = rtv.value
            collData = theTerrain.pixelData[int((1+our_player.position[0])*512)][int((1+our_player.position[1])*512)]
            if theTerrain.check_nodes(our_player.position,0.1):
                main_loop = False
                break
            if collData == 0:
                our_player.position = theTerrain.this_node
                our_player.velocity = (0,0)
                our_player.theta = math.atan2(theTerrain.this_node[1]-theTerrain.next_node[1],theTerrain.this_node[0]-theTerrain.next_node[0])
                our_player.speed = 0
                score -= 5
                offSound.play()

            #print(len(theTerrain.enemies))
            for en in theTerrain.enemies:

                if util3d.distance2(en.pos,our_player.position) < (en.radius+our_player.radius)**2 and not en.collected:
                    print("Collected Enemy")
                    badSound.play()
                    #en.move(0,0.05,0)
                    en.collected = True
                    score -= 3

            for hp in theTerrain.happy:

                if util3d.distance2(hp.pos,our_player.position) < (hp.radius + our_player.radius)**2 and not hp.collected:
                    goodSound.play()
                    print("Collected happy")
                    #hp.move(0,0.05,0)
                    hp.collected = True
                    score += 1


            #print(score)
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

            gluLookAt(our_player.position[0]+math.cos(our_player.theta)/10, 0.05, our_player.position[1]+math.sin(our_player.theta)/10, our_player.position[0]-math.cos(our_player.theta)/30, 0, our_player.position[1]-math.sin(our_player.theta)/30, 0, 1,0)



            util3d.drawTerrain(theTerrain)
            for t in theTerrain.trees:
                util3d.renderSprite(t)
            #playerTree.setPos(our_player.position[0],0,our_player.position[1])
            #util3d.renderSprite(playerTree)
            for spr in theTerrain.enemies:
                if not spr.collected:

                    util3d.renderSprite(spr)
            for spr in theTerrain.happy:
                if not spr.collected:

                    util3d.renderSprite(spr)

            theCar.draw(our_player.position,our_player.theta)
            util3d.enableFlat()
            glLoadIdentity()
            if theVal[0] == 1:

                theFaces.draw("happy")
            if theVal[0] == 0:
                theFaces.draw("neutral")
            if theVal[0] == -1:
                theFaces.draw("sad")
            pygame.display.flip()
            pygame.display.set_caption("score= " + str(score))




            #handle playing input
            #draw game



    rtv.go = False
    theThread.join()
    pygame.quit()
    push_score((name,score))


if __name__ == "__main__":
    startGame()



