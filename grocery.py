class Grocery:
	def __init__(self, name, type = None, price = 0.00):
		self.name = name
		self.type = type
		self.price = price
		
	def __repr__(self):
		return self.name

	def get_name(self):
		return self.name
	
	def get_type(self):
		return self.type
		
	def set_price(self, price):
		self.price = price
		
	def get_price(self):
		return self.price
		
	