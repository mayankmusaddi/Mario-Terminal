class Write:
	@staticmethod
	def toArray(design):
		file = open(design,"r")
		a = []
		for line in file:
			a.append(str(line)[:-1])
		return a