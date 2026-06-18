class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#created Child class
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#inheriting init of parent class 
#class Student(Person):
#  def __init__(self, fname, lname):
#    Person.__init__(self, fname, lname)


#super() function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
