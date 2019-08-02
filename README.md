# Python's Disciples Game - OxfordHack 2018
![Gameplay picture](https://github.com/JC-G/Pythons-Disciples/blob/master/Game.png)


A racing game in which you control your car with facial expressions and leaning.
We used a CNN to be able to extract emotion and face location data from webcam input in real time, so the game is hands-free.

- Collect the Windows-like icons to gain points and avoid the Apple-like icons!
- Try to complete 3 laps as quickly as possible!
- The track is procedurally generated.
- High score feature included.

> Coded in python/pygame/opengl.

## Table of Contents

- [Methodology](#methodology)
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)


---

## Methodology

The main novelty of our game (driving the car without using your hands) was achieved as following:

- We used open-source code implementing a Convolutional Neural Network (CNN) to achieve emotion recognition.
- We used basic linear algebra to interpret correctly the movements of the head which were also tracked using libraries.
- We figured out that the easier expressions to detect were "happy" and "angry", thus we made the car got forwards when the user looked happy, backwards when angry.

After that, to provide some additional features to the game:

- We created objects that increase a player's score when collected ("windows") and objects that must be avoided since they decrease the score and slow down the car("apples").
- We generated random tracks and random placements of windows/apples so that the user has a unique experience in every race.
- We created a json file to keep track of high scores.

---

## Installation

### Clone

- Clone this repo to your local machine using  ```https://github.com/JC-G/Pythons-Disciples.git```

### Setup

- Run GUI.py

- Enter your username in the terminal

- Click Play Game in the Main Menu

---

## Features

- Play Game
- High-scores 
- Main Menu

![Menu picture](https://github.com/JC-G/Pythons-Disciples/blob/master/Menu.png)

- Credits


## Team

- Man Hon Fan
- Joseph Chambers-Graham
- Charalampos Kokkalis
- Gabriela Van Bergen

---


## License

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
