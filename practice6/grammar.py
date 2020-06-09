
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

	def print(self):
		print('Terminals    : {}'.format(self.terminals))
		print('Non Terminals: {}'.format(self.nonterminals))
