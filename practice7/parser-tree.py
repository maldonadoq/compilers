from grammar import Grammar
import readline

class Node:
	label = ""
	children = list()
	father = None
	brother = None

	def __init__(self):
		self.label = label
		self.children = []
		self.father = father
		self.brother = 

class ParserTree:
	def __init__(self, grammar):
		self.grammar = grammar
		self.grammar.runFirsts()
		self.grammar.runFollows()

		self.table = dict()
		self.fillTable()

	def fillTable(self):
		self.table = {}

		for nonterminal in self.grammar.nonterminals:
			tmp = {}
			for terminal in self.grammar.firsts[nonterminal]:
				if(terminal != 'lambda'):
					pr = self.grammar.findProduction(nonterminal, terminal)
					if(pr is not None):
						tmp[terminal] = pr
				else:
					for terminal2 in self.grammar.follows[nonterminal]:
						tmp[terminal2] = ['lambda']

			self.table[nonterminal] = tmp

	def getQueue(self, sentence):
		q = []
		tokens = sentence.split()

		for token in tokens:
			if(token in self.grammar.nonterminals or token in self.grammar.terminals):
				q.append(token)
			else:
				return None
		
		return q

	def op1(self):
		pass

	def op2(self):
		pass

	def op3(self):
		pass

	def recognizeSentence(self, sentence):
		q = self.getQueue(sentence)

		if(q is None):
			return 'Invalid Tokens!'

		q.append(self.grammar.dolar)

		s = []
		s.append(self.grammar.dolar)
		s.append(self.grammar.init)

		while(len(q) != 0 and len(s) != 0):
			if(q[0] == s[-1]):
				q.pop(0)
				s.pop()

				print('op 2')
			else:
				tmp = s.pop()

				if(tmp in self.table and q[0] in self.table[tmp]):
					for tok in self.table[tmp][q[0]][::-1]:
						if(tok != 'lambda'):
							s.append(tok)
							print('op 1')
					else:
						print('op 3')

		if(len(q) == 0 and len(s) == 0):
			return 'Sentence Accepted!'
		
		return 'Sentence Not Accepted'


if __name__ == '__main__':
	gramm = Grammar(filename='grammar2.txt', init='E')
	parser = ParserTree(gramm)

	r = parser.recognizeSentence('id + id')
	print(r)

	""" while(True):
		line = input('sentence: ')

		if(line == 'q'):
			break    
			
		r = parser.recognizeSentence(line)
		print('  ', r) """