from .errors import IllegalCharError
from .position import Position
from .token import Token, Type

digits = "0123456789"


class Lexer:
	def __init__(self):
		pass

	def clear(self, fn, text):
		self.fn = fn
		self.text = text
		self.pos = Position(-1, 0, -1, fn, text)
		self.current_char = None
		self.advance()

	def advance(self):
		self.pos.advance(self.current_char)

		if(self.pos.idx < len(self.text)):
			self.current_char = self.text[self.pos.idx]
		else:
			self.current_char = None

	def getNumber(self):
		num = ''
		dot = 0
		pos_start = self.pos.copy()

		while(self.current_char != None and self.current_char in digits+'.'):
			if(self.current_char == '.'):
				if(dot == 1):
					break

				dot += 1
				num += '.'
			else:
				num += self.current_char

			self.advance()

		if(dot == 0):
			return Token(Type.tint.name, int(num), pos_start, self.pos)
		else:
			return Token(Type.tfloat.name, float(num), pos_start, self.pos)

	def scanner(self, fn, text):
		self.clear(fn, text)

		tokens = []
		while(self.current_char != None):
			if(self.current_char in ' \t'):
				self.advance()
			elif(self.current_char in digits):
				tokens.append(self.getNumber())
			elif(self.current_char == '+'):
				tokens.append(Token(Type.tplus.name, pos_start=self.pos))
				self.advance()
			elif(self.current_char == '-'):
				tokens.append(Token(Type.tminus.name, pos_start=self.pos))
				self.advance()
			elif(self.current_char == '*'):
				tokens.append(Token(Type.tmul.name, pos_start=self.pos))
				self.advance()
			elif(self.current_char == '/'):
				tokens.append(Token(Type.tdiv.name, pos_start=self.pos))
				self.advance()
			elif(self.current_char == '('):
				tokens.append(Token(Type.tlpar.name, pos_start=self.pos))
				self.advance()
			elif(self.current_char == ')'):
				tokens.append(Token(Type.trpar.name, pos_start=self.pos))
				self.advance()
			else:
				pos_start = self.pos.copy()
				ch = self.current_char
				self.advance()
				return [], IllegalCharError(pos_start, self.pos, "'" + ch + "'")

		tokens.append(Token(Type.teof.name, pos_start=self.pos))
		return tokens, None
