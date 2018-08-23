from characters import *

class Missile(Character):
	def __init__(self,life,x,y,*designs):
		super(Missile,self).__init__(life,x,y,*designs)

	def attack(self,enemy):
		if self.x+self.width == enemy.x and self.y+self.height > enemy.y and enemy.y+enemy.height > self.y:
			enemy.life-=1
			self.life-=1

class Fire(Character):
	def __init__(self,life,x,y,*designs):
		super(Fire,self).__init__(life,x,y,*designs)

	def attack(self,enemy):
		if self.x == enemy.x and self.y+self.height > enemy.y and enemy.y+enemy.height > self.y:
			enemy.life-=1
			self.life-=1