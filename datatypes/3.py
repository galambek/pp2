#multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#slicing
b = "Hello, World!"
print("\n", b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

#modifying
c = "Hello, World!"
print("\n", c.upper())
c = "Hello, World!"
print(c.lower())
#removing whitespaces
c = " Hello, World! "
print(c.strip()) # returns "Hello, World!"
#replacing
c = "Hello, World!"
print(c.replace("H", "J"))

#splitting
d = "Hello, World!"
print("\n", d.split(",")) # returns ['Hello', ' World!']
print("\n", d.split("l")) # returns ['He', '', 'o, Wor', 'd!']


