from grocery import Grocery

class ShoppingList:
	def __init__(self, list = None):
		self.categories = []
		if list == None:
			self.list = []
		else:
			self.list = list
			
	def __repr__(self):
		total = ""
		for item in self.list:
			total += item.get_name() + "\n"
		return total
		
	def add(self, item):
		if type(item) == Grocery:
			self.list.append(item)
		else:
			print("Invalid item")
		
	def delete(self, item):
		if item in self.list:
			self.list.remove(item)
			
	def list_categories(self):
		for item in self.list:
			if item.get_type() not in self.categories:
				self.categories.append(item.get_type())
			
	def print_categories(self):
		for category in self.categories:
			print(category)
			for item in self.list:
				if item.get_type() == category:
					print("\t" + item.get_name())
			print()