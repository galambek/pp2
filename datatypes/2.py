x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x, "is", type(x))
print(y, "is", type(y))
print(z, "is", type(z))

#int
x = 1
y = 35656222554887711
z = -3255522

print(x, "is", type(x))
print(y, "is", type(y))
print(z, "is", type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(x, "is", type(x))
print(y, "is", type(y))
print(z, "is", type(z))

#scientific numbers with e
x = 35e3
y = 12E4
z = -87.7e100

print(x, "is", type(x))
print(y, "is", type(y))
print(z, "is", type(z))

#complex
x = 3+5j
y = 5j
z = -5j

print(x, "is", type(x))
print(y, "is", type(y))
print(z, "is", type(z))


#type conversion 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print("\n Type conversion")
print(a, "is", type(a))
print(b, "is", type(b))
print(c, "is", type(c))


