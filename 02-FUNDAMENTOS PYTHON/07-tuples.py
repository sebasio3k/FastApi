my_tuple = (1, 2, 3, 4, 5, "Bastian", "Ramirez", "Hernandez", True, False, [1, 2, 3], {"name": "Bastian", "last_name": "Ramirez"}, 2.5)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(1))

# my_tuple[0] = 10 # This will raise an error because tuples are immutable

weekday_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(weekday_tuple)
