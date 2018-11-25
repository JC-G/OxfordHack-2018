import util3d
import gentrack
import gentrackdata

class Terrain:
    def __init__(self):
        gentrack.run()
        self.pixelData = gentrackdata.getPixelData()
        self.img = util3d.makeTexture("track.png")[0]
        self.nodes = gentrack.storedResults
        print(len(self.pixelData))

        self.next_node = self.nodes[1]
        self.next_i = 1

    def check_nodes(self,pos,r):
        if (self.next_node[1]-pos[1])**2 + (self.next_node[0]-pos[0])**2 < 10:
            self.next_i+=1
            self.next_i %= len(self.nodes)
            self.next_node = self.nodes[i]
            print("Node Advanced to",self.next_i)


