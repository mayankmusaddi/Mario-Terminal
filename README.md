# Python Terminal Mario

## Introduction

This game is the replica of the typical Mario Game. It has been written using Python 3. It uses no external (other than standard) python libraries. The game is also bundled with an easy to use level generator. This game has great moving animations and is very easily editable. Important to note that the game has been tested on **ONLY** Linux-based OSs, and _may not_ work on Windows.

## Structure

The application demonstrates inheritance, encapsulation, polymorphism as well as overloading.
- Each "object" is a derived class of the `Element` class.
- Each player/enemy is a derived class of the `Character` class.
- The `level` has its own class and and captures all objects placed on it.
- All classes directly/indirectly inherit the `Element` class

## Running the program

- Simply replace the first line of `main.py` with the location of your python installation
	- `#!/usr/bin/env python`
- Running the program is easy
	- `./main.py`
- Or you can directly run the game through terminal using the command
	- `python3 main.py`
- To use the level generator use the command
	- `python3 levelGenerator.py`

## Controls

- Controls follow traditional classic titles (W,S,A,D)
- To fire you need to collect the fire powerup which is the character `>` , after which you can fire by pressing `f`
- Health pickup is denoted by `H` block which you could pick by hammering it up by making the mario jump underneath it
- Similarly the `?` block will give you coins
- Other rules are similar to the classic mario
- At every level you will face the boss enemy at the end which you are required to kill to win and move to the castle
- The level generator has controls listed in the top after you execute it.
- To quit, press `q`
- NOTE : Directory structure is not to be changed as it may affect functionality

## File Structure

.
 * [main.py](./main.py)
 * [levelGenerator.py](./levelGenerator.py)
 * [element.py](./element.py)
 * [characters.py](./characters.py)
 * [level.py](./level.py)
 * [player.py](./player.py)
 * [enemies.py](./enemies.py)
 * [weapons.py](./weapons.py)
 * [action.txt](./action.txt)
 * [getch.txt](./getch.txt)
 * [README.md](./README.md)
 * [designs](./designs)
 * [levels](./levels)