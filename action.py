class Write:
	@staticmethod
	def toArray(design):
		file = open(design,"r")
		a = []
		for line in file:
			a.append(str(line)[:-1])
		return a

class Action:
	@staticmethod
	def printGame(arr):
		for line in arr:
			print(line[:80])

	@staticmethod
	def place(arr,toPlace,x,y):
		arrP=[]
		cy=0
		for line in arr:
			if(cy>=y and cy<y+len(toPlace)):
				l = line[:x] + toPlace[cy-y] + line[ (x+len(toPlace[cy-y])) :]
			else:
				l = line
			arrP.append(l)
			cy+=1
		return arrP