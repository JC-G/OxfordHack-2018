import util3d
import gentrack
import gentrackdata

class Terrain:
    def __init__(self):
        gentrack.run()
        self.pixelData = gentrackdata.getPixelData()
        self.img = util3d.makeTexture("track.png")[0]

