class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, res):
		if(isinstance(res, ParseResult)):
			if(res.error):
				self.error = res.error
			
			return res.node
		
		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, _error):
		self.error = _error
		return self

class RunTimeResult:
	def __init__(self):
		self.value = None
		self.error = None

	def register(self, res):
		if(res.error):
			self.error = res.error

		return res.value

	def success(self, value):
		self.value = value
		return self

	def failure(self, _error):
		self.error = _error
		return self