from action import *

class Element:
	def __init__(self,x,y,*designs):
		self.x = x
		self.y = y
		self.designArr=[]
		self.design=[]
		self.height=0
		self.width=0
		if len(designs) > 0:
			for file in designs:
				self.designArr.append(Write.toArray(file))
			self.design=self.designArr[0]
			self.height = len(self.design)
			self.width = len(self.design[0])