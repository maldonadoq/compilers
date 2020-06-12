class Production:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return '{} := {}'.format(self.left, self.right)

class Grammar:
	def __init__(self, filename, init='E'):
		self.terminals 		= []
		self.nonterminals	= []
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
				self.nonterminals.append(left)

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
					if(pr not in self.terminals):
						self.terminals.append(pr)

		self.productions.append(Production(left, right))

	def getProductions(self):
		return self.productions	

	def getProduction(self, left):
		tmp = []

		for pr in self.productions:
			if(pr.left == left):
				tmp.append(pr.right)

		return tmp

	def findProduction(self, nonterm, term):
		productions = self.getProduction(nonterm)

		if(len(productions) == 1):
			return productions[0]

		for production in productions:
			if(term in production):
				return production

		return None

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
		for left in self.nonterminals:
			productions = self.getProduction(left)
			for production in productions:
				for i, token in enumerate(production):
					if(token == non):
						if(i < (len(production) - 1)):
							tmp = production[i+1]
							if(tmp in self.terminals):
								self.follows[non].add(production[i+1])
							elif(tmp in self.nonterminals):
								for f in self.firsts[tmp]:
									if(f != 'lambda'):
										self.follows[non].add(f)
								self.follows[non] |= self.follows[left]
						else:
							if token in self.nonterminals:
								self.follows[non] |= self.follows[left]

	def runFollows(self):
		self.terminals.append(self.dolar)
		
		for nonterminal in self.nonterminals:
			self.follows[nonterminal] = set()		
		self.follows[self.init].add(self.dolar)
		
		for nonterminal in self.nonterminals:
			self.runFollow(nonterminal)
