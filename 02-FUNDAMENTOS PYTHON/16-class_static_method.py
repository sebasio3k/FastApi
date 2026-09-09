
class Person:
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        
    
    # class method
    def change_species(self, new_species):
        self.species = new_species
        
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    @classmethod
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def is_older(age):
        return age >= 18
        
        
# initializing an instance of the Person class:
person1 = Person("Bastian", 29)
person2 = Person("Rogelio", 28)

print(person1.species)
print(person2.species)
# person1.change_species("Homo neanderthalensis")
Person.change_species("Homo neanderthalensis")
print(person1.species)
print(person2.species)
print(person1.get_species())
print(person2.get_species())

print(Person.is_older(17))
print(person1.is_older(person1.age))
print(person2.is_older(person2.age))