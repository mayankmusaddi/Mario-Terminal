from element import *
import os

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

	def printOnTop(self,*characters):
		temp = self.design
		for toPlace in characters:
			arrP=[]
			cy=0
			for line in temp:
				if ( cy >= round(toPlace.y) and cy< round(toPlace.y)+len(toPlace.design)):
					l = line[ : toPlace.x ] + toPlace.design[ cy-round(toPlace.y) ] + line[ (toPlace.x+len(toPlace.design[ cy-round(toPlace.y) ])) :]
				else:
					l = line
				arrP.append(l)
				cy+=1
			temp = arrP
		os.system("clear")
		for line in temp:
			print(line[self.pos: self.pos+80])