a = 0.4
class Neuron:
	wx1 = 0
	wx2 = 0
	wx3 = 0
	su = 0
	y = 0
	def __init__(self, ws):
		self.w1 = ws[0]
		self.w2 = ws[1]
		self.w3 = ws[2]

	def setWs(self, ws):
		self.w1 = ws[0]
		self.w2 = ws[1]
		self.w3 = ws[2]

	def getWs(self):
		return [self.w1, self.w2, self.w3]	

	def exec(self, joins):
		wx1 = joins[0] * self.w1
		wx2 = joins[1] * self.w2
		wx3 = joins[2] * self.w3

		su = wx1 + wx2 + wx3

		if su > 0:
			y = 1
		else:
			y = -1

		return y

def getExpected(expectecd, y):
	if len(expectecd) == 1:
		return expectecd[0]
	else:
		return y

def error(neuron, row, joins):
	y1 = neuron.exec([row["joins"][0], row["joins"][1], row["joins"][2]])
	y2 = neuron.exec([row["joins"][0], row["joins"][1], row["joins"][2]])
	y3 = neuron.exec([row["joins"][0], row["joins"][1], row["joins"][2]])

	w1 = neuron.w1 + a * (getExpected(row["expected"], y1) - y1) * joins[0]
	w2 = neuron.w2 + a * (getExpected(row["expected"], y2) - y2) * joins[1]
	w3 = neuron.w3 + a * (getExpected(row["expected"], y3) - y3) * joins[2]

	return [round(w1, 2), round(w2, 2), round(w3, 2)]

def train(neuron, table ,times):
	finalWs = neuron.getWs()
	for i in range(times):
		for j in range(len(table)):
			rowTest = table[j]
			joins = rowTest["joins"]
			result = round(neuron.exec(joins),2)
			if (result != getExpected(rowTest["expected"], result)):
				#print("error en  " + str(j))
				correct = error(neuron, rowTest, joins)
				#print(correct)
				finalWs = correct 
				neuron.setWs(correct)
				break
			else:
				pass
				#print("Las entradas " + str(joins) + " generan " + str(result) + " y se esperaba " + str(rowTest["expected"]))
	return finalWs



table1 = {
	0 : {
		"joins" : [-1, -1, -1],
		"expected" : [1]
	},
	1 : {
		"joins" : [-1, -1, 1],
		"expected" : [1]
	},
	2 : {
		"joins" : [-1, 1, -1],
		"expected" : [-1]
	},
	3 : {
		"joins" : [-1, 1, 1],
		"expected" : [-1]
	},
	4 : {
		"joins" : [1, -1, -1],
		"expected" : [1]
	},
	5 : {
		"joins" : [1, -1, 1],
		"expected" : [1]
	},
	6 : {
		"joins" : [1, 1, -1],
		"expected" : [-1]
	},
	7 : {
		"joins" : [1, 1, 1],
		"expected" : [-1]
	}
}


table2 = {
	0 : {
		"joins" : [-1, -1, -1],
		"expected" : [-1]
	},
	1 : {
		"joins" : [-1, -1, 1],
		"expected" : [-1, 1]
	},
	2 : {
		"joins" : [-1, 1, -1],
		"expected" : [-1]
	},
	3 : {
		"joins" : [-1, 1, 1],
		"expected" : [-1, 1]
	},
	4 : {
		"joins" : [1, -1, -1],
		"expected" : [-1, 1]
	},
	5 : {
		"joins" : [1, -1, 1],
		"expected" : [1]
	},
	6 : {
		"joins" : [1, 1, -1],
		"expected" : [-1, 1]
	},
	7 : {
		"joins" : [1, 1, 1],
		"expected" : [1]
	}
}


table3 = {
	0 : {
		"joins" : [-1, -1, -1],
		"expected" : [-1]
	},
	1 : {
		"joins" : [-1, -1, 1],
		"expected" : [1]
	},
	2 : {
		"joins" : [-1, 1, -1],
		"expected" : [-1]
	},
	3 : {
		"joins" : [-1, 1, 1],
		"expected" : [-1]
	},
	4 : {
		"joins" : [1, -1, -1],
		"expected" : [1]
	},
	5 : {
		"joins" : [1, -1, 1],
		"expected" : [1]
	},
	6 : {
		"joins" : [1, 1, -1],
		"expected" : [-1]
	},
	7 : {
		"joins" : [1, 1, 1],
		"expected" : [1]
	}
}

ws = [0.3, 0.5, 0.7]

neuron1 = Neuron(ws)
neuron2 = Neuron(ws)
neuron3 = Neuron(ws)




print("Pesos calculados para la neurona 1 " + str(train(neuron1, table1, 1000)))
print("Pesos calculados para la neurona 2 " + str(train(neuron2, table2, 1000)))
print("Pesos calculados para la neurona 3 " + str(train(neuron3, table3, 1000)))
