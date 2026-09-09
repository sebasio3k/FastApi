
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."  
    
    def work(self):
        return f"{self.name} is working."
    


# Initializing an instance of the Person class:
person1 = Person("Bastian", 29)
person2 = Person("Rogelio", 28)

print(person1)
print(person2)
print(person1.greet())
print(person2.greet())
print(person1.work())
print(person2.work())
