import os,time
from characters import *
from getch import *

class GamePlay:

	def main():
		os.system("clear")
		print("Enter level : ",end='')
		levelname = input()
		level = Level(0,0,levelname+".txt")
		mario = Character(3,2,10,"mario1.txt","mario2.txt","mario3.txt")
		mario.cannotCross=['T','|','/','\\','`']

		while True:
			os.system("clear")

			level.printOnTop(mario)
			mario.gravity(level)
			choice = getch()

			if choice is 'a':
				if mario.x > level.pos:
					mario.moveLeft(level)

			elif choice is 'd':
				if mario.x < level.pos+(40)-mario.width:
					mario.moveRight(level)
				else:
					if mario.moveRight(level):
						level.pos+=1

			elif choice is 'w':
				mario.jumpTime = time.time()
				if mario.velocity is 0:
					mario.velocity = 16

			elif choice is 'x':
				break
		print(mario.coins)

	main()
