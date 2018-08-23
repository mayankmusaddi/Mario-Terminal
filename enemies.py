from characters import *
from weapons import *

class Goomba(Character):
	def __init__(self,life,x,y,*designs):
		self.direction = -1
		self.slow = 0.5
		super(Goomba,self).__init__(life,x,y,*designs)

	def move(self,structure):
		if time.time()-self.spawnTime > self.slow:
			if self.direction == -1:
				if not self.moveLeft(structure):
					self.direction = 1
			else:
				if not self.moveRight(structure):
					self.direction = -1
			self.spawnTime = time.time()

class Boss(Character):
	def __init__(self,life,x,y,*designs):
		self.slow = 2
		self.fires=[]
		self.fireTime=time.time()
		self.health = "  ####################################"
		super(Boss,self).__init__(life,x,y,*designs)

	def move(self,structure):
		if time.time()-self.spawnTime > self.slow:
			self.y = random.randrange(12)
			self.spawnTime = time.time()

	def gravity(self,structure):
		pass

	def attack(self):
		if time.time()-self.fireTime > self.slow*2:
			for i in range(4,7):
				fire = Fire(1,self.x - abs(i%5 - 2),self.y+i,"./designs/fire.txt")
				fire.cannotCross=['T','|','/','\\','`']
				self.fires.append(fire)
			self.fireTime = time.time()