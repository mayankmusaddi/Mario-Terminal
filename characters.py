import time
from action import *

floorPos = 18
g=-14

class Element:
	def __init__(self,x,y,*designs):
		self.x = x
		self.y = y
		self.designArr=[]
		for file in designs:
			self.designArr.append(Write.toArray(file))
		self.design=self.designArr[0]
		self.height = len(self.design)
		self.width = len(self.design[0])

class Character(Element):
	def __init__(self,life,x,y,*designs):
		self.life=life
		self.posture=0
		self.dn=1
		self.velocity=0
		self.jumpTime=0
		super(Character,self).__init__(x,y,*designs)

	def motion(self):
		self.posture+=self.dn
		if self.posture is (len(self.designArr)-1) or self.posture is 0:
			self.dn*=-1
		self.design=self.designArr[self.posture]

	def moveRight(self):
		self.motion()
		self.x+=1

	def moveLeft(self):
		self.motion()
		self.x-=1

	def moveUp(self):
		self.y-=1

	def moveDown(self):
		self.y+=1

	def gravity(self,game):
		t = time.time()-self.jumpTime

		self.y -= t*(self.velocity + (0.5 * g * t)) 
		self.velocity += g*t
		self.jumpTime=time.time()
		# if (self.y+self.height) >= floorPos:
			# self.velocity=0
			# self.y = floorPos - self.height

		if game[round(self.y+self.height)][self.x+round(self.width/2)] is 'T':
			self.velocity=0
			self.y = floorPos - self.height

class Background(Element):
	def __init__(self,x,y,*designs):
		super(Background,self).__init__(x,y,*designs)

	def moveForward(self):
		arrR=[]
		for line in self.design :
			l = line[1:]+line[:1]
			arrR.append(l)
		self.design = arrR