class NumberNode:
	def __init__(self, token):
		self.token = token

		self.pos_start = self.token.pos_start
		self.pos_end = self.token.pos_end
	
	def __repr__(self):
		return '{}'.format(self.token)

class BinOpNode:
	def __init__(self, left_node, op_token, right_node):
		self.left_node = left_node
		self.op_token = op_token
		self.right_node = right_node

		self.pos_start = self.left_node.pos_start
		self.pos_end = self.right_node.pos_end

	def __repr__(self):
		return '({},{},{})'.format(self.left_node, self.op_token, self.right_node)

class UnaryOpNode:
	def __init__(self, op_token, node):
		self.op_token = op_token
		self.node = node

		self.pos_start = self.op_token.pos_start
		self.pos_end = node.pos_end

	def __repr__(self):
		return '({},{})'.format(self.op_token, self.node)