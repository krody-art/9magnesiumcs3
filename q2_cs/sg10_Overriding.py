class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(self.name, "eat")

  def make_sound(self):
    print(self.name, "make sound")

class Lion(Animal):
  def make_sound(self):
    print(self.name, "Roars")

  def eat(self):
    print(self.name, "eat Fresh meat")


class Elephant(Animal):
  def make_sound(self):
    print(self.name, "Trumphets")

  def eat(self):
    print(self.name, "Grass and Fruit")

class Monkey(Animal):
  def make_sound(self):
    print(self.name, "Chatters")

  def eat(self):
    print(self.name, "Banana")


#lion1 = Lion("Simba)
#lion1.make_sound
#lion1.eat
