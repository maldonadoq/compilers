
class Grammar:
	productions = {}
	terminals = set()
	nonterminals = set()

	def getProduction(self):
		pass

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
		return self.productions[_left]

	def printGrammar(self):
		print('Terminals     : {}'.format(self.terminals))
		print('Non Terminals : {}\n'.format(self.nonterminals))

		for left in self.productions:
			print('{:3}:'.format(left), end=' ')

			for right in self.productions[left]:
				print(right, end=' ')
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

	gramm.printGrammar()

	left = "E"
	right = gramm.getProduction(left)
	print('\n{:3}: {}'.format(left, right))
