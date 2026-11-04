class Animal:            #Creates a class called Animal
  def __init__(self, name):  # Initializes self and value (attributes)
    self.name = name  # Declares self.name to name

  def eat(self):    # Creates a function called "eat" (Methods)
    return self.name + " eat" # Returns the value of name and the value "eat".

  def make_sound(self): # Creates a function called "make_sound" (Methods)
    return self.name + " make sound"  # Returns the value of name and a value, which is "make sound".

class Lion(Animal):   #Creates a subclass called "Lion" and inherits the attributes of the class "Animal"
  @make_sound.getter
  def make_sound(self):  #Same function as class "Animal"
    return self.name + " roars loudly!"   # As you can observe here, we replace the value of animal with its own value---

  def eat(self):
    return self.name + " eats fresh meat"


class Elephant(Animal):
  def make_sound(self):
    return self.name + " trumpets!"

  def eat(self):
    return self.name + " eats grass and fruit."

class Monkey(Animal):
  def make_sound(self):
    return self.name + " chatters!"

  def eat(self):
    return self.name + " eats bananas."

    


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
