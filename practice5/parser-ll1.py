from grammar import Grammar, toString
import readline

class ParserLL1:
	def __init__(self, grammar):
		self.grammar = grammar
		self.table = dict()

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

	def print(self):
		print('Parsing Table LL1')

		print(' '*5, end='')
		for col in self.grammar.terminals:
			if(col != 'lambda'):
				print('{:8}'.format(col), end='')
		print('\n', '-'*(len(self.grammar.terminals)*8))

		for row in self.grammar.nonterminals:
			print('{:4}|'.format(row), end='')
			for col in self.grammar.terminals:
				if(col != 'lambda'):
					if(col in self.table[row]):
						print('{:8}'.format(toString(self.table[row][col])), end='')
					else:
						print(' '*8, end='')
			print()

		""" for row in self.table:
			print(row)
			print('  {}'.format(self.table[row])) """

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
	parser.print()

	""" while(True):
		line = input('sentence: ')

		if(line == 'q'):
			break    
			
		r = parser.recognizeSentence(line)
		print('  ', r) """