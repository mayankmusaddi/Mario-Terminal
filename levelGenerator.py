import os,time
from action import *
from characters import *
from getch import *

class LevelGenerator:

	def main():
		os.system('clear')
		print("1. Edit Existing")
		print("2. Start from Scratch")
		ch = input()
		filename = "level"
		if ch is '1': 
			print("Enter Level Name : ",end='')
			filename = input()

		level = Level(0,0,filename+".txt")

		enemies = []
		enemiesstr = []

		while True:
			os.system("clear")
			level.printOnTop(*enemies)

			choice = input()
			if choice is 'b':
				obj = Character(0,level.pos,0,"brick.txt")
				obj.cannotCross=['T','/','\\','`','-']
			elif choice is 'c':
				obj = Character(0,level.pos,0,"coin.txt")
				obj.cannotCross=['T','|','/','\\','`','-']
			elif choice is 's':
				obj = Character(0,level.pos,0,"spring.txt")
				obj.cannotCross=['|','/','\\','`','-']
			elif choice is 't':
				obj = Character(0,level.pos,0,"tunnel.txt")
				obj.cannotCross=['T','|','/','\\','`','-']
			elif choice is 'p':
				obj = Character(0,level.pos,0,"pit.txt")
				obj.cannotCross=['/','\\','`','-']
			elif choice is 'm':
				obj = Character(0,level.pos,0,"coinbrick.txt")
				obj.cannotCross=['T','/','\\','`','-']
			elif choice is 'g':
				obj = Character(1,level.pos,0,"goomba1.txt","goomba2.txt")
				obj.cannotCross=['T','|','/','\\','`']
			else:
				break

			while True:
				os.system("clear")

				level.printOnTop(obj,*enemies)
				move = getch()

				if move is 'a':
					if obj.x > level.pos:
						obj.moveLeft(level)
	
				elif move is 'd':
					if obj.x < level.pos+(40)-obj.width:
						obj.moveRight(level)
					else:
						if obj.moveRight(level):
							level.pos+=1
	
				elif move is 'w':
					if obj.y>0:
						obj.moveUp(level)

				elif move is 's':
					if obj.y < 23-obj.height:
						obj.moveDown(level)

				elif move is 'x':
					if choice is 'g':
						enemies.append(obj)
						enemystr = "Character(1,"+str(obj.x)+","+str(obj.y)+",\"goomba1.txt\",\"goomba2.txt\")"
						enemiesstr.append(enemystr)
					else:
						level.place(obj)
					break

		if ch is not '1':
			print("Enter Level Name : ",end='')
			filename = input()

		open(filename+".txt", "w").close()
		file = open(filename+".txt","a")

		open(filename+"Enemy.txt", "w").close()
		enemyfile = open(filename+"Enemy.txt","a")

		for line in level.design:
			file.write(line+"\n")

		for line in enemiesstr:
			enemyfile.write(line+"\n")

	main()