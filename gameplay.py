import os,time
from characters import *
from getch import *

class GamePlay:

	def main():
		while True:
			print("Enter level : ",end='')
			levelname = input()
			try:
				level = Level(0,0,"./levels/"+levelname+".txt")
				break
			except FileNotFoundError:
				print("Level does not Exist!\nCreate your level by command 'python3 levelGenerator.py'")


		mario = Character(3,2,10,"./designs/mario1.txt","./designs/mario2.txt","./designs/mario3.txt")
		mario.cannotCross=['T','|','/','\\','`']

		enemies=[]
		try:
			file = open("./levels/"+levelname+"Enemy.txt","r")
			for line in file:
				goomba = eval(line)
				goomba.cannotCross=['T','|','/','\\','`']
				enemies.append(goomba)
		except:
			pass

		while True:
			os.system("clear")

			mario.gravity(level)
			index=0
			for enemy in enemies:
				enemy.gravity(level)
				
				if (round(mario.y)+mario.height-1 == round(enemy.y)) and mario.x+mario.width > enemy.x and enemy.x+enemy.width > mario.x:
					enemy.life-=1
					if enemy.life == 0:
						del(enemies[index])
						mario.kills +=1
				elif mario.y+mario.height > enemy.y and enemy.y+enemy.height > mario.y and mario.x+mario.width > enemy.x and enemy.x+enemy.width > mario.x :
					mario.life-=1
					mario.spawn(level)
				index+=1

				enemy.move(level)


			level.printOnTop(mario,*enemies)

			if mario.life is 0:
				print("GAME OVER")
				break

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

			elif choice is 'q':
				break
		print(mario.coins)

	os.system("clear")
	main()
 	