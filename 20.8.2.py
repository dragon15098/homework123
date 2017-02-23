def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity
    print("Da them")

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
if "" in new_inventory.keys():
    print("Co strawberries trong dict ")
if new_inventory["strawberries"] == 10:
    print("Co 10 strawberries")
add_fruit(new_inventory, "strawberries", 25)
if new_inventory["strawberries"] == 35:
    print("Co 10 strawberries")
else:
    print("Co ", new_inventory["strawberries"], "qua strawberries")
