import readline

class Grammar:
	productions = {}
	terminals = set()
	nonterminals = set()
	sat = dict()

	def setGrammar(self, _text):
		line = _text.split()
		size = len(line)
		if(size > 1 and line[1] == ":="):
			
			left = line[0]
			if(left in self.nonterminals):
				self.buildProduction(left, line[2:])
			else:
				self.nonterminals.add(left)
				self.productions[left] = []

				if(left in self.terminals):
					self.terminals.remove(left)

				self.buildProduction(left, line[2:])
		else:
			print("Invalid Grammar")

	def buildProduction(self, _left, _producs):

		right = []
		for pr in _producs:			
			if(pr == '|'):
				self.productions[_left].append(right)
				right = []
			else:
				right.append(pr)

				if(pr not in self.nonterminals):
						self.terminals.add(pr)

		self.productions[_left].append(right)

	def getProduction(self, _left):
		if(_left in self.nonterminals):
			return self.productions[_left]
		else:
			if(_left in self.terminals):
				return 'It is terminal Token'
			return 'Do not have Production'

	def fillInSat(self):
		self.sat["E"] = {"(": ["T", "Ep"], "num": ["T", "Ep"], "id": ["T", "Ep"]}
		self.sat["Ep"] = {"+": ["+", "T", "Ep"], "-": ["-", "T", "Ep"], ")": ["lambda"], "$": ["lambda"]}
		self.sat["T"] = {"(": ["F", "Tp"], "num": ["F", "Tp"], "id": ["F", "Tp"]}
		self.sat["Tp"] = {"+": ["lambda"], "-": ["lambda"], "*": ["*", "F", "Tp"], "/": ["/", "F", "Tp"], ")": ["lambda"], "$": ["lambda"]}
		self.sat["F"] = {"(": ["(", "E", ")"], "num": ["num"], "id": ["id"]}

	def printGrammar(self):
		print('Terminals     : {}'.format(self.terminals))
		print('Non Terminals : {}\n'.format(self.nonterminals))

		for left in self.productions:
			print('{:3}:'.format(left), end=' ')

			for right in self.productions[left]:
				print(right, end=' ')
			print()
		
		print()
		for sp in self.sat:
			print('{:3}'.format(sp), end=' ')
			for tok in self.sat[sp]:
				print('{}:{}'.format(tok, self.sat[sp][tok]), end='\t')
			print()


if __name__ == "__main__":
	gramm = Grammar()

	gramm.setGrammar("E := T Ep")
	gramm.setGrammar("Ep := + T Ep")
	gramm.setGrammar("Ep := - T Ep")
	gramm.setGrammar("Ep := lambda")
	gramm.setGrammar("T := F Tp")
	gramm.setGrammar("Tp := * F Tp | / F Tp | lambda")
	gramm.setGrammar("F := ( E ) | num | id")

	gramm.fillInSat()

	gramm.printGrammar()
	print('\n---------------------------------------------\n')

	while(True):
		left = input('query: ')

		if(left == 'q'):
			break    
	
		right = gramm.getProduction(left)
		print('  {:3}: {}'.format(left, right))
