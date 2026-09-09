
class Person:
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self._energy = 100  # Protected attribute
        self.__health = 100  # Private attribute

    # public_method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def work(self):
        return f"{self.name} is working."
    
    # protected_method
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return f"Energy: {self._energy}"
    
    # private_method
    def __eat(self, quantity):
        self._energy += quantity
        return f"Energy: {self._energy}"


# Initializing an instance of the Person class:
person1 = Person("Bastian", 29)
person2 = Person("Rogelio", 28)

print(person1)
print(person2)
print(person1.greet())
print(person2.greet())
print(person1.work())
print(person2.work())

print(person1._energy)
print(person1._waste_energy(20))
print(person1._energy)
# print(person1.__health) # AttributeError

# print(person1.__eat(30))
print(person1._Person__eat(30))
print(person1._energy)

print(person1._Person__health) # Private attribute
