#When you create an object from a class, it inherits all the variables and functions defined inside that class
#__init__() function always runs whenever new object of that class is created
class Person:
  def __init__(self, name, age, city, country):  #self is first parameter of __init__() which is referred as current object
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#skipped del - it just deletes properties of object or even object itself

#class properties vs object properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#youcan also add new properties to object(not to all of them though) or modify existing class properties(which will affect every object)

#without __str__() method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)        #returns this bs <__main__.Person object at 0x00000154EC446900>
print(p1)

#with __str__() method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)       #returns Tobias (36)
print(p1)
