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