from characters import *
from weapons import *

class Mario(Character):
	def __init__(self,life,x,y,*designs):
		self.kills=0
		self.coins=0
		self.gun = False
		self.missiles=[]
		super(Mario,self).__init__(life,x,y,*designs)

	def kill(self,enemy,structure):
		if (round(self.y)+self.height-1 == round(enemy.y)) and self.x+self.width > enemy.x and enemy.x+enemy.width > self.x:
			enemy.life-=1
		elif self.y+self.height > enemy.y and enemy.y+enemy.height > self.y and self.x+self.width > enemy.x and enemy.x+enemy.width > self.x :
			self.life-=1
			self.spawn(structure)

	def attack(self):
		if self.gun is True:
			missile= Missile(1,self.x+5,self.y+2,"./designs/missile.txt")
			missile.cannotCross=['T','|','/','\\','`']
			self.missiles.append(missile)

	def spawn(self,structure):
		self.x=structure.pos+2
		self.y=0
		self.velocity=0

	def tangible(self,structure):
		cy=round(self.y)
		for line in structure.design[ round(self.y) : round(self.y+self.height) ] :

			cx=self.x
			for character in line[self.x:self.x+self.width]:
				space = Element(cx,cy,"./designs/empty.txt")
				if character is '0' or character is '?':
					self.coins+=1
					structure.place(space)
				if character is 'H':
					self.life+=1
					structure.place(space)
				if character is '>':
					self.gun = True
					structure.place(space)
				cx+=1

			if '-' in line[self.x:self.x+self.width]:
				self.velocity=26
				return True

			for character in self.cannotCross:
				if character in line[self.x:self.x+self.width]:
					return False
			cy+=1
		return True	