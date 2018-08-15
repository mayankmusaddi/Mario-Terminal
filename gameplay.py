import os,time
from action import *
from characters import *
from getch import *

class GamePlay:

	def main():
		background = Background(0,0,"background.txt")
		mario = Character(3,35,13,"mario1.txt","mario2.txt","mario3.txt")
		while True:
			os.system("clear")

			game = Action.place(background.design,mario.design,mario.x,round(mario.y))
			Action.printGame(game)

			mario.gravity(game)
			choice = getch()

			if choice is 'a':
				if mario.x > 0:
					mario.moveLeft()

			elif choice is 'd':
				if mario.x < (0.5*background.width)-mario.width:
					mario.moveRight()
				else:
					background.moveForward()
					mario.motion()

			elif choice is 'w':
				mario.jumpTime = time.time()
				if mario.velocity is 0:
					mario.velocity = 14

			elif choice is 'x':
				break

	main()
