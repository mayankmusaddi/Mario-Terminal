import os,time
from characters import *
from player import *
from enemies import *
from weapons import *
from level import *
from element import *
from getch import *

class GamePlay:

	def main():
		while True:
			print("All levels :")
			os.system("ls ./levels/ | grep -oP '^((?!Enemy).)*$' | sed -e 's/\.txt$//'")
			print()
			print("Enter level : ",end='')
			levelname = input()
			try:
				level = Level(0,0,"./levels/"+levelname+".txt")
				break
			except FileNotFoundError:
				print("Level does not Exist!\nCreate your level by command 'python3 levelGenerator.py'")

		mario = Mario(3,2,10,"./designs/mario1.txt","./designs/mario2.txt","./designs/mario3.txt")
		mario.cannotCross=['T','|','/','\\','`']
		lives = Element(3,0)
		coins = Element(26,0)
		kills = Element(49,0)
		score = Element(72,0)
		boss = Boss(10,277,12,"./designs/boss.txt")
		boss.design[0]=boss.health
		boss.cannotCross=['T','|','/','\\','`']
		enemies=[boss]

		try:
			file = open("./levels/"+levelname+"Enemy.txt","r")
			for line in file:
				goomba = eval(line)
				goomba.cannotCross=['T','|','/','\\','`']
				enemies.append(goomba)
		except:
			pass

		while True:

			if mario.x == 321:
				mario.cannotCross=['T']
				winTime = time.time()
			if mario.x == 379:
				print("YOU WIN!!!")
				break

			mario.gravity(level)

			# moving of all the enemies and missile collision
			index=0
			for enemy in enemies:
				enemy.gravity(level)
				enemy.move(level)
				mario.kill(enemy,level)
				for missile in mario.missiles:
						missile.attack(enemy)

				if enemy.life <= 0:
					del(enemies[index])
					mario.kills+=1
				index+=1

			# moving of all the missiles
			index=0
			for missile in mario.missiles:
				if not missile.moveRight(level) or missile.life <=0 or missile.x > level.pos+80:
					del(mario.missiles[index])
				index+=1

			# moving of all the fires
			if level.pos > 200:
				if boss.life > 0:
					boss.attack()
				index=0
				for fire in boss.fires:
					fire.attack(mario)
					if not fire.moveLeft(level) or fire.life <=0 or fire.x < boss.x-70:
						del(boss.fires[index])
					index+=1

			boss.design[0] = boss.health[:boss.life+2]
			lives.design = ["LIVES",str(mario.life)]
			coins.design = ["COINS",str(mario.coins)]
			kills.design = ["KILLS",str(mario.kills)]
			score.design = ["SCORE",str(mario.kills*50+mario.coins*10+level.pos)]
			lives.x=level.pos+3
			coins.x=lives.x+23
			kills.x=coins.x+23
			score.x=kills.x+23
			
			# os.system("clear")
			level.printOnTop(mario,*enemies,*mario.missiles,*boss.fires,lives,coins,kills,score)

			if mario.life <= 0:	
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
				if mario.velocity is 0:
					mario.velocity = 20

			elif choice is 'f':
				mario.attack()

			elif choice is 'h':
				level.pos+=5
				mario.spawn(level)

			elif choice is 'q':
				break
	os.system("clear")
	main()
 	