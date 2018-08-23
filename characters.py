import time,random,os
from element import *

floorPos = 23	
g = -20

class Character(Element):
	def __init__(self,life,x,y,*designs):
		self.life=life
		self.posture=0
		self.dn=1
		self.velocity=0
		self.jumpTime=time.time()
		self.spawnTime = time.time()
		self.cannotCross=[]
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
			if self.life > 0:
				self.spawn(structure)

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
