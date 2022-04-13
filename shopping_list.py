from grocery import Grocery

class ShoppingList:
	def __init__(self, list = None):
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
			
	def calc_line_length(self, name, price):
		taken_space = len(name) + len(str(price))
		empty_space = ""
		if(taken_space < 40):
			for i in range(40 - taken_space):
				empty_space += " "
		return empty_space
	
	def print_categories(self):
		categories = []
		for item in self.list:
			if item.get_type() not in categories:
				categories.append(item.get_type())

		for category in categories:
			print(category)
			for item in self.list:
				if item.get_type() == category:
					print("\t" + item.get_name() + self.calc_line_length(item.get_name(), item.get_price()) + str(item.get_price()))
			print()