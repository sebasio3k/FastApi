user = {"name": "Bastian", "last_name": "Ramirez", "age": 30, "is_alive": True}

print(type(user))
print(user)
print(user["name"])
print(user["last_name"])
print(user["age"])
print(user["is_alive"])

user["is_alive"] = False
print(user)

#values items keys
print(user.values())
print(user.items())
print(user.keys())