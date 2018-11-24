import math

class Player:
    def __init__(self):
        self.position = (0,0)
        self.velocity = (0,0)
        self.acceleration = (0,0)
        self.speed = 0
        self.theta = 0

    def move(self,turnMagnitude,forwards):
        if turnMagnitude == 0 and forwards == 0:
            return
        speed = 0.01
        turnSpeed = 0.01
        self.theta = math.atan2(self.velocity[1],self.velocity[0])
        r = (self.velocity[0]*self.velocity[0]+self.velocity[1]*self.velocity[1])*turnMagnitude*turnSpeed
        self.acceleration = (r*math.cos(self.theta+math.pi/2)+forwards*speed*math.cos(self.theta),r*math.sin(self.theta+math.pi/2)+forwards*speed*math.cos(self.theta))
        self.velocity = (self.velocity[0]+self.acceleration[0],self.velocity[1]+self.acceleration[1])
        self.position = (self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
        print(self.acceleration,self.velocity,self.position)


        #self.theta +=turnMagnitude# math.atan2(self.velocity[1],self.velocity[0])
        #self.position = (self.position[0]+forwards*math.cos(self.theta),self.position[1]+forwards*math.sin(self.theta))

        #self.acceleration = (forwards*math.cos(self.theta)+turnMagnitude*math.cos(self.theta+math.pi/2),forwards*math.sin(self.theta)+turnMagnitude*math.sin(self.theta+math.pi/2))
        #self.velocity = (self.velocity[0]+self.acceleration[0],self.velocity[1]+self.acceleration[1])
        #self.position = (self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
        #p2 = (self.position[0]+turnMagnitude,self.position[1]+forwards)
        #self.theta = math.atan2(forwards,turnMagnitude)
        #self.position = p2



