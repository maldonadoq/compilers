import readline

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter, Context

if __name__ == "__main__":
	lex = Lexer()
	par = Parser()
	inter = Interpreter()
	ctx = Context('<program>')

	while(True):
		line = input('> ')

		if(line == 'q'):
			break

		tokens, error = lex.scanner('<stdin>', line)		

		if(error):
			print('lexer error:', error)
		else:
			print('lexer success:', tokens)
			ast = par.parse(tokens)
			if(ast.error):
				print('parser error:', ast.error)
			else:
				print('parser success:', ast.node)
				res = inter.visit(ast.node, ctx)

				if(res.error):
					print('interpreter error:', res.error)
				else:
					print('interpreter success:', res.value)