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
			
	def fill_line(self, name, price, length = 40):
		taken_space = len(name) + len("{:.2f}".format(price))
		empty_space = ""
		if(taken_space < length):
			for i in range(length - taken_space):
				empty_space += "."
		return empty_space
	
	def make_categories(self):
		categories = []
		total = 0.0
		full_string = ""

		for item in self.list:
			if item.get_type() not in categories:
				categories.append(item.get_type())

		for item in self.list:
			total += item.get_price()

		full_string += "\nShopping List:\n"
		full_string += (40 * "=" + "\n")
		for category in categories:
			full_string += category + ":\n"
			for item in self.list:
				if item.get_type() == category:
					full_string += (" " + item.get_name() + self.fill_line(item.get_name(), item.get_price(), 39) + "{:.2f}".format(item.get_price()) + "\n")
			full_string += "\n"
		full_string += (40 * "=" + "\n")
		full_string += ("Total:" + self.fill_line("Total:", total) + "{:.2f}".format(total) + "\n")
		return full_string
	
	def make_shopping_list_txt(self):
		with open("shopping_list.txt", 'w') as file:
			file.write(self.make_categories())