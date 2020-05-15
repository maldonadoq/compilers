import readline

dolar = '$'

class Grammar:
	productions = {}

	init = ''

	terminals = set()
	nonterminals = set()
	
	first_tmp = []

	def setInit(self, init):
		self.init = init

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
		
		return None

	def printGrammar(self):
		print('Terminals     : {}'.format(self.terminals))
		print('Non Terminals : {}\n'.format(self.nonterminals))

		for left in self.productions:
			print('{:3}:'.format(left), end=' ')

			for right in self.productions[left]:
				print(right, end=' ')
			print()

	def getFirst(self, left):
		productions = self.getProduction(left)

		for production in productions:
			if(production[0] in self.nonterminals):
				self.getFirst(production[0])
			else:
				self.first_tmp.append(production[0])

	def getFirsts(self):
		firsts = {}
		for nonterminal in self.nonterminals:			
			self.getFirst(nonterminal)
			firsts[nonterminal] = self.first_tmp.copy()

			self.first_tmp.clear()

		return firsts

	def getFollows(self):
		follows = {}
		follows[self.init] = [dolar]

		

		print(follows)

	def buildTable(self):
		pass

if __name__ == "__main__":
	gramm = Grammar()

	gramm.setInit('E')
	gramm.setGrammar('E := T Ep')
	gramm.setGrammar('Ep := + T Ep')
	gramm.setGrammar('Ep := - T Ep')
	gramm.setGrammar('Ep := lambda')
	gramm.setGrammar('T := F Tp')
	gramm.setGrammar('Tp := * F Tp | / F Tp | lambda')
	gramm.setGrammar('F := ( E ) | num | id')

	gramm.getFollows()
