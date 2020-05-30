def toString(ls):
	tmp = ''
	for i in ls:
		tmp = tmp + i + ' '
	
	return tmp

first_tmp	= []

class Production:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return '{} := {}'.format(self.left, self.right)

class Grammar:
	def __init__(self, filename, init='E'):
		self.terminals 		= set()
		self.nonterminals	= set()
		self.productions	= []

		self.firsts		= dict()
		self.follows	= dict()

		self.init = init
		self.dolar = '$'
		self.readGrammar(filename)

	def readGrammar(self, filename):
		file_grammar = open(filename,'r')
		lines = file_grammar.readlines()

		for line in lines:
			self.setGrammar(line)

		file_grammar.close()

	def setGrammar(self, line):
		tokens = line.split()
		size = len(tokens)
		
		if(size > 1 and tokens[1] == ":="):
			
			left = tokens[0]
			if(left in self.nonterminals):
				self.buildProduction(left, tokens[2:])
			else:
				self.nonterminals.add(left)

				if(left in self.terminals):
					self.terminals.remove(left)

				self.buildProduction(left, tokens[2:])
		else:
			print("Invalid Grammar")

	def buildProduction(self, left, production):
		right = []
		for pr in production:
			if(pr == '|'):
				self.productions.append(Production(left, right))
				right = []
			else:
				right.append(pr)

				if(pr not in self.nonterminals):
					self.terminals.add(pr)

		self.productions.append(Production(left, right))

	def getProductions(self):
		return self.productions	

	def getProduction(self, left):
		tmp = []

		for pr in self.productions:
			if(pr.left == left):
				tmp.append(pr.right)

		return tmp

	def runFirst(self, left):
		production = self.getProduction(left)

		for token in production:
			if(token[0] in self.nonterminals):
				self.runFirst(token[0])
			else:
				first_tmp.append(token[0])

	def runFirsts(self):
		for nonterminal in self.nonterminals:
			self.runFirst(nonterminal)
			self.firsts[nonterminal] = first_tmp.copy()

			first_tmp.clear()

	def runFollow(self, non):
		if(len(self.follows[non]) == 0):
			if(non == self.init):
				self.follows[non].add(self.dolar)

			for left in self.nonterminals:
				productions = self.getProduction(left)
				for production in productions:
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
		for nonterminal in self.nonterminals:
			self.follows[nonterminal] = set()
			
		for nonterminal in self.nonterminals:
			self.runFollow(nonterminal)

	""" def runFollows(self):
		for nonterminal in self.nonterminals:
			self.follows[nonterminal] = set()

		self.follows[self.init].add(self.dolar)
			
		for nonterminal in self.nonterminals:			
			productions = self.getProduction(nonterminal)
			for production in productions:

				aux = self.follows[nonterminal]
				for token in production:
					if token in self.follows:
						self.follows[token].union(aux)
						aux = self.firsts[token] """

	def print(self):
		print('Terminals    : {}'.format(self.terminals))
		print('Non Terminals: {}\n'.format(self.nonterminals))

		print('Productions:')
		for pr in self.productions:
			print(pr)		

		print('\n{:8}{:^15}{:^15}'.format('Token', 'Firsts', 'Follows'))
		print('-'*38)
		for non in self.nonterminals:
			print('{:8}{:^15}{:^15}'.format(
				non,
				toString(self.firsts[non]),
				toString(self.follows[non])
			))

if __name__ == "__main__":
	gramm = Grammar(filename='grammar.txt', init='E')
	gramm.runFirsts()
	gramm.runFollows()

	gramm.print()