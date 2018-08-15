import os,time
from action import *
from getch import *

class GamePlay:

	def main():
		bg = Write.toArray("background.txt")
		sm1 = Write.toArray("mario1.txt")
		sm2 = Write.toArray("mario2.txt")
		sm3 = Write.toArray("mario3.txt")
		smario = [sm1,sm2,sm3]
		pos=[35,13]
		posture=0
		dirc=1
		jump=False

		while True:
			os.system("clear")
			sm = smario[posture]

			if jump is True:
				ctime = time.time()
				t=ctime-jtime
				if rise is True and (10*t+(1/2)*t*t) > step:
					step+=1
					pos[1]-=1
					if step > 7:		
						rise = False
						jtime=time.time()
						step=0
				if rise is False:
					if (10*t*t) > step:
						step+=1
						pos[1]+=1
						if step > 7:
							jump = False

			pa = Action.place(bg,sm,pos)
			Action.printGame(pa)
			choice = getch()
			if choice is 'a':
				bg = Action.leftCycle(bg)

				posture+=(dirc)
				if posture is 2:
					dirc=-1
				if posture is 0:
					dirc=1

			elif choice is 'd':
				bg = Action.rightCycle(bg)

				posture+=(dirc)
				if posture is 2:
					dirc=-1
				if posture is 0:
					dirc=1

			elif choice is 'w':
				if jump is False:
					jump=True
					rise=True
					step=0
					jtime=time.time()
					cpy=jtime

			elif choice is 'x':
				break
	main()