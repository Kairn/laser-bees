# Laser Bees (2D Game)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT Licence](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://opensource.org/licenses/mit-license.php)

Pilot an advanced military spacecraft equipped with laser weapons capable of upgrading to destroy waves of alien controlled battleships and claim final victory! This game is a tribute to another indie game developed in 1999.

## Launch the Game
### Compatibilities
Windows 7 & 8.1 & 10

*Due to Pygame not being compatible with Python3 on Linux, a Windows OS is required.*
### Prerequisites
* Python 3.4.3 (not tested with newer versions)

	[Python 3.4.3 Official Download Page](https://www.python.org/downloads/release/python-343/)

* Pygame 1.9.3 (not tested with older versions)

	`pip install pygame`

    [Pygame Installation Instructions](https://www.pygame.org/wiki/GettingStarted)

### Install and Run
1. Download the [repository](https://github.com/Kairn/laser-bees-new) as a .zip file or using git clone.
2. Extract the .zip file.
3. Open the game directory (laser-bees-master) and double click *laser_bees.py*.

	Alternatively, open a terminal in the game directory and run the following command:

    `python laser_bees.py`

## How to Play
### Basics
* Press ENTER to start a new game.
* Press ESC to quit the game.
* Press P to pause/resume the game.
* Press E to go back to the start screen.

### Controls
* Hold down LEFT (<) or RIGHT (>) arrow keys to move your ship.
* Press SPACE to fire your weapon.

### The Rules
Your goal is to destroy the enemy spaceships that appear on every stage. You start your mission with a level 1 spacecraft that can fire only one shot at a time and have only **1 HP**. But you have the opportunity to become stronger before you face the wrath of the enemy's elite forces. Starting from stage 1-2, on every other stage, a purple treasure chest will spawn within the enemy group, and it drops a star which will upgrade your ship by one level if you destroy it. You will have increased firepower and HP every time your receive an upgrade until reaching the max level (level 10). But be careful, if you are hit by an enemy's attack, you ship will be downgraded by one level or be destroyed if you are only level 1. You will be declared victorious after clearing all 30 stages, or a blazing death will mark the end of your mission.

### *Turn On Cheat Mode*
1. Go to the game directory and open *laser_bees.py* with a text editor.
2. Change line 29 to the following:

	`game_settings = settings.Settings(debug=True)`

*Cheat mode allows the player to manipulate the game in ways forbidden by the rules.*

### *Cheat Controls*
* Press Z to upgrade your ship by one level.
* Press X to downgrade your ship by one level.
* Press G to make your ship invincible.
* Press N to clear all enemies and advance to the next stage.
* Press 1 to spawn a type A enemy.
* Press 2 to spawn a type B enemy.
* Press 3 to spawn a type C enemy.
* Press 4 to spawn a type D enemy.
* Press 0 to spawn a treasure chest.

## Acknowledgments
Special thanks to some of the anonymous contributors on [DeviantArt](https://www.deviantart.com/) and [The Spriters Resource](https://www.spriters-resource.com) for providing this project with in-game object sprites and background images.
