import math
import numpy
class Player:
    def __init__(self):
        self.position = (0,0)
        self.velocity = (0,0)
        self.acceleration = (0,0)
        self.speed = 0
        self.theta = 0

    def move(self,turnMagnitude,forwards):
        #if turnMagnitude == 0 and forwards == 0:
            #pass
            #return
        speed = 0.01
        turnSpeed = 0.01
        max_speed = 0.1


        #self.theta = math.atan2(self.velocity[1],self.velocity[0])
        #r = (self.velocity[0]*self.velocity[0]+self.velocity[1]*self.velocity[1])*turnMagnitude*turnSpeed
        #self.acceleration = (r*math.cos(self.theta+math.pi/2)+forwards*speed*math.cos(self.theta),r*math.sin(self.theta+math.pi/2)+forwards*speed*math.cos(self.theta))
        #self.velocity = (self.velocity[0]+self.acceleration[0],self.velocity[1]+self.acceleration[1])
        #self.position = (self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
        #print(self.acceleration,self.velocity,self.position)


        self.theta -=turnMagnitude*math.sqrt(math.fabs(self.speed))*numpy.sign(self.speed)*40# math.atan2(self.velocity[1],self.velocity[0])

        dt=1/60
        self.speed += forwards*dt

        self.speed -= self.speed*self.speed*10.1*numpy.sign(self.speed)
        if self.speed > max_speed:
            self.speed = max_speed

        self.velocity = (math.cos(self.theta)*self.speed,math.sin(self.theta)*self.speed)


        self.position = (self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])




