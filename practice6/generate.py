from grammar import Grammar

class Generate:
	def __init__(self):
		self.names = {}
		
		self.names['+'] = 'Plus'
		self.names['-'] = 'Minus'
		self.names['lambda'] = 'Lambda'
		self.names['*'] = 'Mult'
		self.names['/'] = 'Div'
		self.names['('] = 'LPar'
		self.names[')'] = 'RPar'
		self.names['num'] = 'Num'
		self.names['id'] = 'Ident'

	def createFiles(self, gramm):
		# Terminals
		for t in gramm.terminals:
			tfile = open('src/' + self.names[t] + 'Terminal.py', 'w')

			tmp = \
'''
class {}Terminal(AbstractExpressionT):
	#value
	def interprets():
		return value
'''.format(self.names[t])
			
			tfile.write(tmp)
			tfile.close()

		# NonTerminals
		for nt in gramm.nonterminals:
			tfile = open('src/' + nt + 'NonTerminal.py', 'w')

			tmp = \
'''
class {}NonTerminal(AbstractExpressionNT):
	#dict<nameClase, object>
	def interprets(val1, val2, val3):
		return (0,0,0)
'''.format(nt)
			
			tfile.write(tmp)
			tfile.close()

if __name__ == "__main__":
	gramm = Grammar(filename='grammar.txt', init='E')
	gen = Generate()

	gen.createFiles(gramm)