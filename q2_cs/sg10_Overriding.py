class Animal:            #Creates a class called Animal
  def __init__(self, name):  # Initializes self and value (attributes)
    self.name = name  # Declares self.name to name

  def eat(self):    # Creates a function called "eat" (Methods)
    return self.name + " eat" # Returns the value of name and the value "eat".

  def make_sound(self): # Defines a function called "make_sound" (Methods)
    return self.name + " make sound"  # Returns the value of name and a value, which is "make sound".

class Lion(Animal): #Creates a subclass called "Lion" and inherits the attributes of the class "Animal"
  
  
  def make_sound(self):  # Same method as class "Animal"
    return self.name + " roars loudly!"   # As you can observe here, we replace the value of animal with its own value.

  def eat(self): # Same method as class "Animal"
    return self.name + " eats fresh meat" # We replace the value of animal with its own value.


class Elephant(Animal): # Creates another subclass called "Elephant" that inherits from the superclass "Animal". This class inherits no values/attributes from the class "Lion".
  def make_sound(self): # Defines a function called "make_sound" (Methods) 
    return self.name + " trumpets!" # Returns the name and replaces the value of the superclass with its unique value.

  def eat(self):
    return self.name + " eats grass and fruit."

class Monkey(Animal): # Creates another subclass called "Elephant" that inherits from the superclass "Animal". This class inherits no values/attributes from the class "Lion".
  def make_sound(self): # Defines a function called "make_sound" (Methods) 
    return self.name + " chatters!" # Returns the name and replaces the value of the superclass with its own unique value.

  def eat(self):
    return self.name + " eats bananas." # Returns the name and replaces the value of the superclass with its own unique value.

    

# ---Example Outputs---
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")
