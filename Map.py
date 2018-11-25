import util3d
import gentrack
import gentrackdata
import random
enemyNumber = 10
happyNumber = 10
class Terrain:
    def __init__(self):
        self.enemies = []
        self.happy = []

        gentrack.run()
        self.pixelData = gentrackdata.getPixelData()
        self.img = util3d.makeTexture("track.png")[0]
        self.nodes = gentrack.storedResults

        for x in range(happyNumber):
            pos = (0,0)
            while self.pixelData[pos[0]][pos[1]] != 1:
                pos = (random.randint(0,1023),random.randint(0,1023))

            self.happy.append(util3d.Sprite3d("windows.png",pos[0]/512-1,0,pos[1]/512-1,0.01))

        for x in range(enemyNumber):
            pos = (0,0)
            while self.pixelData[pos[0]][pos[1]] != 1:
                pos = (random.randint(0,1023),random.randint(0,1023))

            self.enemies.append(util3d.Sprite3d("apple.png",pos[0]/512-1,0,pos[1]/512-1,0.01))


        #print(len(self.pixelData))

        self.next_node = self.nodes[1]
        self.this_node = self.nodes[0]
        self.next_i = 1

    def check_nodes(self,pos,r):
        if (self.next_node[1]-pos[1])**2 + (self.next_node[0]-pos[0])**2 < 0.3:
            self.next_i+=1
            self.next_i %= len(self.nodes)
            self.this_node = self.next_node
            self.next_node = self.nodes[self.next_i]

            print("Node Advanced to",self.next_i)


