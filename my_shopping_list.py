from shopping_list import ShoppingList
from grocery import Grocery

# File for testing purposes

my_list = ShoppingList()
bread = Grocery("Bread", "Dry Goods", 1.38)
milk = Grocery("Milk", "Dairy", 3.69)
eggs = Grocery("Eggs", "Dairy", 2.99)
pizza = Grocery("Pepperoni Pizza", "Frozen", 4.99)
ice_cream = Grocery("Vanilla Ice Cream", "Frozen", 3.49)
canned_peas = Grocery("Canned Peas", "Canned Goods", 1.00)

my_list.add(bread)
my_list.add(milk)
my_list.add(eggs)
my_list.add(pizza)
my_list.add(ice_cream)
my_list.add(canned_peas)

print(my_list.make_categories())
my_list.make_shopping_list_txt()