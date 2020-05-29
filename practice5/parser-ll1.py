from grammar import Grammar
import readline

class ParserLL1:
	def __init__(self, grammar):
		self.grammar = grammar
		self.table = dict()

	def fillTable(self):
		''' self.table = {}

		for left in self.grammar.nonterminals:
			productions = gramm.getProduction(left)
			for production in productions:
				for token in production:
					#print(token)
					if(token != 'lambda'):
						for el in self.grammar.firsts[token]:
							self.table[left, el] = token
					else:
						for el in self.grammar.follows[left]:
							self.table[left, el] = token
				print()

		print(self.table) '''

		self.table['E'] = {'(': ['T', 'Ep'], 'num': ['T', 'Ep'], 'id': ['T', 'Ep']}
		self.table['Ep'] = {'+': ['+', 'T', 'Ep'], '-': ['-', 'T', 'Ep'], ')': ['lambda'], '$': ['lambda']}
		self.table['T'] = {'(': ['F', 'Tp'], 'num': ['F', 'Tp'], 'id': ['F', 'Tp']}
		self.table['Tp'] = {'+': ['lambda'], '-': ['lambda'], '*': ['*', 'F', 'Tp'], '/': ['/', 'F', 'Tp'], ')': ['lambda'], '$': ['lambda']}
		self.table['F'] = {'(': ['(', 'E', ')'], 'num': ['num'], 'id': ['id']}

	def getQueue(self, sentence):
		q = []
		tokens = sentence.split()

		for token in tokens:
			if(token in self.grammar.nonterminals or token in self.grammar.terminals):
				q.append(token)
			else:
				return None
		
		return q

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
			else:
				tmp = s.pop()

				if(tmp in self.table and q[0] in self.table[tmp]):
					for tok in self.table[tmp][q[0]][::-1]:
						if(tok != 'lambda'):
							s.append(tok)

		if(len(q) == 0 and len(s) == 0):
			return 'Sentence Accepted!'
		
		return 'Sentence Not Accepted'


if __name__ == '__main__':
	gramm = Grammar(filename='grammar.txt', init='E')
	gramm.runFirsts()
	gramm.runFollows()

	parser = ParserLL1(gramm)
	parser.fillTable()

	while(True):
		line = input('sentence: ')

		if(line == 'q'):
			break    
			
		r = parser.recognizeSentence(line)
		print('  ', r)
