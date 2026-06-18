#skipped obvious def parts

#assigning default values to function
def myfunc(x, num = 67):
    x += num
    print("now x is", x)
    return x


x = 0
myfunc(x, )
myfunc(myfunc(x, ), 1)
myfunc(myfunc(myfunc(x, ), 1), 10)
print(x)

#def myfunc(x, /)   means that function has positional arguments only
#def myfunc(*, x)   means that function has keyword arguments only
#you can combine them

#*args
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#you can combine *args with regular arguments - but they must come first

#**kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#order of parameters: regular, *args, **kwargs

#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)   #without * it will not work out(only 1 argument-list is sent)
print(result)


#SCOPE
#functions within some function can access all of it's local variables
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() 

#global keyword
x = 300
def myfunc():
  global x
  x += 1

myfunc()

print(x)

#nonlocal - makes variable belong to outer function
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x           #here we can't use global, because x is not global variable, it is local
    x = "hello"
  myfunc2()
  return x

print(myfunc1())