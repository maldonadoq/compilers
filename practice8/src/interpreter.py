from .token import Type
from .values import Number
from .results import RunTimeResult

class Context:
	def __init__(self, display_name, parent=None, parent_entry_pos=None):
		self.display_name = display_name
		self.parent = parent
		self.parent_entry_pos = parent_entry_pos

class Interpreter:
	def visit(self, node, context):
		method_name = 'visit_{}'.format(type(node).__name__)
		method = getattr(self, method_name, self.no_visit)

		return method(node, context)

	def no_visit(self, node, context):
		raise Exception('No visit_{} method difined'.format(type(node).__name__))

	def visit_NumberNode(self, node, context):
		return RunTimeResult().success(
			Number(node.token.value).set_context(context).set_pos(node.pos_start, node.pos_end)
		)

	def visit_BinOpNode(self, node, context):
		res = RunTimeResult()

		left = res.register(self.visit(node.left_node, context))
		if(res.error):
			return res

		right = res.register(self.visit(node.right_node, context))
		if(res.error):
			return res

		if(node.op_token.type == Type.tplus.name):
			result, error = left.added_by(right)
		elif(node.op_token.type == Type.tminus.name):
			result, error = left.subbed_by(right)
		elif(node.op_token.type == Type.tmul.name):
			result, error = left.multed_by(right)
		elif(node.op_token.type == Type.tdiv.name):
			result, error = left.dived_by(right)

		if(error):
			return res.failure(error)
		else:
			return res.success(result.set_pos(node.pos_start, node.pos_end))

	def visit_UnaryOpNode(self, node, context):	
		res = RunTimeResult()
		number = res.register(self.visit(node.node, context))

		if(res.error):
			return res
		
		error = None

		if(node.op_token.type == Type.tminus.name):
			number, error = number.multed_by(Number(-1))

		if(error):
			return res.failure(error)
		else:
			return res.success(number.set_pos(node.pos_start, node.pos_end))