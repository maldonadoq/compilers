
dolar = '$'
first_tmp = []

def toString(ls):
	tmp = ''
	for i in ls:
		tmp = tmp + i + ' '
	
	return tmp

class Grammar:
	init = 'E'	
	
	def setInit(self, init):
		self.init = init
		self.terminals    = set()
		self.nonterminals = set()

		self.productions = dict()
		self.firsts      = dict()
		self.follows     = dict()
		self.sat         = dict()

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

	def runFirst(self, left):
		production = self.getProduction(left)

		for token in production:
			if(token[0] in self.nonterminals):
				self.runFirst(token[0])
			else:
				first_tmp.append(token[0])

	def runFirsts(self):
		self.firsts.clear()
		for nonterminal in self.nonterminals:
			self.runFirst(nonterminal)
			self.firsts[nonterminal] = first_tmp.copy()

			first_tmp.clear()

	def runFollow(self, non):
		if(len(self.follows[non]) == 0):
			if(non == self.init):
				self.follows[non].add(dolar)

			for left in self.productions:
				for production in self.productions[left]:
					for i, token in enumerate(production):
						if(token == non):
							if(i < len(production) - 1):
								if(production[i+1] in self.terminals):
									self.follows[non].add(production[i+1])
								else:
									for first in self.firsts[production[i+1]]:
										self.follows[non].add(first)
							else:
								if(non != left):
									self.runFollow(left)

									for follow in self.follows[left]:
										self.follows[non].add(follow)

	def runFollows(self):
		self.follows.clear()
		for nonterminal in self.nonterminals:
			self.follows[nonterminal] = set()
			
		for nonterminal in self.nonterminals:
			self.runFollow(nonterminal)

	def fillInSat(self):
		self.sat["E"] = {"(": ["T", "Ep"], "num": ["T", "Ep"], "id": ["T", "Ep"]}
		self.sat["Ep"] = {"+": ["+", "T", "Ep"], "-": ["-", "T", "Ep"], ")": ["lambda"], "$": ["lambda"]}
		self.sat["T"] = {"(": ["F", "Tp"], "num": ["F", "Tp"], "id": ["F", "Tp"]}
		self.sat["Tp"] = {"+": ["lambda"], "-": ["lambda"], "*": ["*", "F", "Tp"], "/": ["/", "F", "Tp"], ")": ["lambda"], "$": ["lambda"]}
		self.sat["F"] = {"(": ["(", "E", ")"], "num": ["num"], "id": ["id"]}

	def print(self):
		print('Terminals    : {}'.format(self.terminals))
		print('Non Terminals: {}\n'.format(self.nonterminals))

		print('Productions:')
		for left in self.productions:
			print('   {:3}:'.format(left), end=' ')

			for i,right in enumerate(self.productions[left]):
				if(i == len(self.productions[left])-1):
					print(toString(right), end=' ')
				else:
					print(toString(right), end=' | ')
			print()

		print('\n{:8}{:^15}{:^15}'.format('Token', 'Firsts', 'Follows'))
		print('-'*38)
		for non in self.nonterminals:
			print('{:8}{:^15}{:^15}'.format(
				non,
				toString(self.firsts[non]),
				toString(self.follows[non])
			))

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

	gramm.fillInSat()
	gramm.runFirsts()
	gramm.runFollows()

	gramm.print()