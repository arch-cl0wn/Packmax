from _3dbp import Bin, Item, Items_List, bp3D, get_items_total_volume
# create bin
bin = Bin("Container1", 500, 300, 400)

# create items
items_list = Items_List()
items_list.add_item(Item("Item01", 20, 20, 30))
items_list.add_item(Item("Item02", 10, 40, 10))
items_list.add_item(Item("Item03", 20, 40, 10))
items_list.add_item(Item("Item04", 20, 20, 20))
items_list.add_item(Item("Item05", 10, 10, 10))
items_list.add_item(Item("Item06", 30, 20, 10))
items_list.add_item(Item("Item07", 30, 10, 20))
items_list.add_item(Item("Item08", 30, 10, 10))
items_list.add_item(Item("Item09", 10, 20, 10))
items_list.add_item(Item("Item10", 10, 20, 10))
items_list.add_item(Item("Item11", 10, 10, 10))
items_list.add_item(Item("Item12", 20, 10, 20))

print("BEFORE packing:")
for item in items_list.items:
    item.print_data()
print("---------------------------------------------------\n")

print("There are", len(items_list.items), "items and the total volume of items is", get_items_total_volume(items_list.items))
bin.print_data()

# packing
bp3D(bin, items_list.items)

print("\nAFTER packing:")
for item in bin.items:
    item.print_data()
print("---------------------------------------------------\n")

bin.print_data()