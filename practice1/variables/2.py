#global and local variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




#global keyword

def myfunc2():
  global y
  y = "terrible"

#must call this function 
myfunc2()

print("Python is " + y)

