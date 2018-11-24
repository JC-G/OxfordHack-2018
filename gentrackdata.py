from PIL import Image
from glob import glob
import numpy as np

def getPixelData():
    track = Image.open("track.png","r")
    width, height = track.size
    pixelValues = list(track.getdata())
    pixelValues = np.array(pixelValues).reshape((width, height, 4))
    arr = []

    for y in range(len(pixelValues)):
        arr.append([])
        for x in range(len(pixelValues[0])):
            if 200 in pixelValues[x][y]:
                arr[-1].append(2)
            elif 104 in pixelValues[x][y]:
                arr[-1].append(1)
            else:
                arr[-1].append(0)
    return arr

if __name__ == "__main__":
    print(getPixelData())