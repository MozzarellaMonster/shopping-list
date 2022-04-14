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
		else:
			print("Item not found")
			
	def calc_line_length(self, name, price, length = 40):
		taken_space = len(name) + len("{:.2f}".format(price))
		empty_space = ""
		if(taken_space < length):
			for i in range(length - taken_space):
				empty_space += "."
		return empty_space
	
	def print_categories(self):
		categories = []
		total = 0.0
		
		for item in self.list:
			if item.get_type() not in categories:
				categories.append(item.get_type())

		for item in self.list:
			total += item.get_price()

		print("\nShopping List:")
		print(40 * "=" + "\n")
		for category in categories:
			print(category + ":")
			for item in self.list:
				if item.get_type() == category:
					print(" " + item.get_name() + self.calc_line_length(item.get_name(), item.get_price(), 39) + "{:.2f}".format(item.get_price()))
			print()
		print(40 * "=")
		print("Total:" + self.calc_line_length("Total:", total) + "{:.2f}".format(total))