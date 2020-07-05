from .token import Type
from .nodes import NumberNode, BinOpNode, UnaryOpNode
from .errors import InvalidSyntaxError
from .results import ParseResult


class Parser:
	def __init__(self):
		pass
	
	def clear(self, tokens):
		self.tokens = tokens
		self.token_idx = -1
		self.advance()

	def advance(self):
		self.token_idx += 1

		if(self.token_idx < len(self.tokens)):
			self.current_token = self.tokens[self.token_idx]
		
		return self.current_token
	
	def factor(self):
		res = ParseResult()
		token = self.current_token

		if(token.type in (Type.tplus.name, Type.tminus.name)):
			res.register(self.advance())
			factor = res.register(self.factor())

			if(res.error):
				return res
			
			return res.success(UnaryOpNode(token, factor))

		elif(token.type in (Type.tint.name, Type.tfloat.name)):
			res.register(self.advance())
			return res.success(NumberNode(token))
		
		elif(token.type == Type.tlpar.name):
			res.register(self.advance())
			expr = res.register(self.expr())

			if(res.error):
				return res
			
			if(self.current_token.type == Type.trpar.name):
				res.register(self.advance())
				return res.success(expr)
			else:
				return res.failure(InvalidSyntaxError(
					self.current_token.pos_start, self.current_token.pos_end,
					"Expected ')'"
				))

		return res.failure(InvalidSyntaxError(
			token.pos_start, token.pos_end,
			"Expected Int or Float"
		))

	def term(self):
		return self.bin_op(self.factor, (Type.tmul.name, Type.tdiv.name))

	def expr(self):
		return self.bin_op(self.term, (Type.tplus.name, Type.tminus.name))

	def bin_op(self, func, ops):
		res = ParseResult()
		left = res.register(func())

		if(res.error):
			return res

		while(self.current_token.type in ops):
			op_token = self.current_token
			res.register(self.advance())

			right = res.register(func())

			if(res.error):
				return res

			left = BinOpNode(left, op_token, right)

		return res.success(left)

	def parse(self, tokens):

		self.clear(tokens)

		res = self.expr()
		if(not res.error and self.current_token.type != Type.teof.name):
			return res.failure(InvalidSyntaxError(
				self.current_token.pos_start, self.current_token.pos_end,
				"Expected '+', '-', '*' or '/'"
			))

		return res