#Parameters
def hello(greet, name):
    print(f"{greet}, {name}!")

#Arguments
hello("Hello", "Alice")
hello("Hi", "Bob")

#Default parameters


def hello2(name ,greet="Hello"):
    
    print(f"{greet}, {name}!")

hello2("Alice")
hello2(greet="Hi", name = "Bob")

def big_function(*args, **kwargs):
    
    print(args)
    print(kwargs)

big_function(1, 2, 3, name="Bastian", last_name="Hernandez")
