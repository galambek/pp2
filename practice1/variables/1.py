x = 5
y = 5.5
z = 'c'

print(x) ; print(type(x))
print(y) ; print(type(y))
print(z) ; print(type(z))

#casting
x = float(x)
print("x type changed")
print(type(x))

#assigning tricks
a, b, c, = "orange", "banana", "apple"
print(a)
print(b)
print(c)
a = b = c = "monkey"
print(a)
print(b)
print(c)

#unpacking list
fruits = ["apple", "banana", "orange"]
a, b, c = fruits
print(a)
print(b)
print(c)

#output tricks
print(a, b, c)
print(a + b + c) #same data type
print(x + y)
print(x, a) #different data types