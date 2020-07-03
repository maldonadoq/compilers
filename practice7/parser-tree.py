from grammar import Grammar
import readline

class Node:
	def __init__(self, label, father=None, brother=None):
		self.label = label
		self.children = list()
		self.father = father
		self.brother = brother

class ParserTree:
	def __init__(self, grammar):
		self.grammar = grammar
		self.grammar.runFirsts()
		self.grammar.runFollows()

		self.table = dict()
		self.fillTable()

		self.root = None

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

	def op1(self, node, childrens):
		if(node):
			for ch in childrens:
				node.children.append(Node(ch, node))

			size = len(node.children)
			for i in range(size):
				if(i < size - 1):
					node.children[i].brother = node.children[i+1]

			return node.children[0]

		else:
			return None

	def op2(self, node):
		if(node):
			if(node.brother):
				return node.brother
			else:
				if(node.father):
					return self.op2(node.father)
				else:
					return None
		else:
			return None

	def op3(self, node):		
		if(node):
			node.children.append(Node('lambda', node))
			return self.op2(node)
		else:
			return None

	def recognizeSentence(self, sentence):
		q = self.getQueue(sentence)

		if(q is None):
			return 'Invalid Tokens!'

		q.append(self.grammar.dolar)

		s = []
		s.append(self.grammar.dolar)
		s.append(self.grammar.init)

		self.root = Node(self.grammar.init)

		while(len(q) != 0 and len(s) != 0):
			if(q[0] == s[-1]):
				q.pop(0)
				s.pop()

				self.root = self.op2(self.root)
			else:
				tmp = s.pop()

				if(tmp in self.table and q[0] in self.table[tmp]):
					symb = self.table[tmp][q[0]]

					if(symb == ['lambda']):
						self.root = self.op3(self.root)
					else:
						for tok in symb[::-1]:
							s.append(tok)
						self.root = self.op1(self.root, symb)
				else:
					break

		if(len(q) == 0 and len(s) == 0):
			return 'Sentence Accepted!'
		
		return 'Sentence Not Accepted'


if __name__ == '__main__':
	gramm = Grammar(filename='grammar1.txt', init='E')
	parser = ParserTree(gramm)

	while(True):
		line = input('sentence: ')

		if(line == 'q'):
			break    
			
		r = parser.recognizeSentence(line)
		print('  ', r)