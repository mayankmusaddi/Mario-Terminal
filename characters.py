import time
from action import *

floorPos = 22
g= -14

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
		self.jumpTime=time.time()
		self.cannotCross=[]
		self.coins=0
		super(Character,self).__init__(x,y,*designs)

	def motion(self):
		self.posture+=self.dn
		if self.posture is (len(self.designArr)-1) or self.posture is 0:
			self.dn*=-1
		if len(self.designArr) is 1:
			self.posture = 0
		self.design=self.designArr[self.posture]

	def moveRight(self,structure):
		self.motion()
		self.x+=1
		if not self.tangible(structure):
			self.x-=1
			return False
		return True


	def moveLeft(self,structure):
		self.motion()
		self.x-=1
		if not self.tangible(structure):
			self.x+=1
			return False
		return True

	def moveUp(self,structure):
		self.y-=1
		if not self.tangible(structure):
			self.y+=1
			return False
		return True

	def moveDown(self,structure):
		self.y+=1
		if not self.tangible(structure):
			self.y-=1
			return False
		return True

	def tangible(self,structure):
		cy=round(self.y)
		for line in structure.design[ round(self.y) : round(self.y+self.height) ] :

			cx=self.x
			for character in line[self.x:self.x+self.width]:
				if character is '0' or character is '?':
					self.coins+=1
					space = Element(cx,cy,"empty.txt")
					structure.place(space)
				cx+=1

			if '-' in line[self.x:self.x+self.width]:
				self.velocity=23
				return True

			for character in self.cannotCross:
				if character in line[self.x:self.x+self.width]:
					return False
			cy+=1
		return True

	def gravity(self,structure):

		if self.y >= floorPos :
			self.life -=1
			self.x=structure.pos+2
			self.y=10
			self.velocity=0

		t = time.time()-self.jumpTime
		by = self.y
		self.y -= t*(self.velocity + (0.5 * g * t)) 
		self.velocity += g*t
		self.jumpTime=time.time()
		if self.y < 0:
			self.y=0

		if not self.tangible(structure):
			self.y=by
			self.velocity = 0
			return False
		return True

class Level(Element):

	def __init__(self,x,y,*designs):
		super(Level,self).__init__(x,y,*designs)
		self.pos=0

	def moveForward(self):
		arrR=[]
		for line in self.design :
			l = line[1:]+line[:1]
			arrR.append(l)
		self.design = arrR

	def print(self):
		for line in self.design:
			print(line[self.pos:self.pos+80])

	def place(self,toPlace):
		arrP=[]
		cy=0
		for line in self.design:
			if ( cy>=toPlace.y and cy< toPlace.y+len(toPlace.design)):
				l = line[:toPlace.x] + toPlace.design[cy-toPlace.y] + line[ (toPlace.x+len(toPlace.design[cy-toPlace.y])) :]
			else:
				l = line
			arrP.append(l)
			cy+=1
		self.design=arrP

	def printOnTop(self,top):
		cy=0
		for line in self.design:
			if cy >= round(top.y) and cy < round(top.y)+len(top.design):
				print((line[:top.x]+top.design[cy-round(top.y)]+line[top.x+len(top.design[cy-round(top.y)]) : ])[self.pos:self.pos+80])
			else:
				print(line[self.pos:self.pos+80])
			cy+=1