list_number = [1, 2, 3, 4, 5]
list_string = ["Bastian", "Ramirez", "Hernandez"]
list_mixed = [1, 2, 3, "Bastian", "Ramirez", "Hernandez", True, False, [1, 2, 3], {"name": "Bastian", "last_name": "Ramirez"}, 2.5]
shopping_cart = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

print(type(list_number))
print(type(list_string))
print(type(list_mixed))
print(type(shopping_cart))


# methods
print(len(list_number))
print(list_number)
print(list_number.count(1))

print(list_number)
list_number.append(6)
print(list_number)
list_number.insert(0, 0)
print(list_number)
list_number.remove(1)
print(list_number)
list_number.pop(0)
print(list_number)
list_number.reverse()
print(list_number)
list_number.sort()
print(list_number)
list_number.clear()
print(list_number)