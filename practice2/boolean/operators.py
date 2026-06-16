#floor division & exponentiation
x = 12
y = 5
print(x / y)
print(x // y)
print(x ** y)


#those are bitwise assignment operators: <<=, >>=, &=, ^=, |=
x = 2
print(x & 8)


#walrus operator(assins value as =, and returns that value) :=
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)):
    print(f"List has {count} elements")

#it won't work out if we write it like this:
#if (count = len(numbers)):
#    print(f"List has {count} elements")



#ternary operator(short "if-else" and "elif" statement)

z = "WEEKDAY" if x == 2 else "naaahhhhh"

print(z)


#in statements we can use and, or, not as logical operators

#Identity operators is, is not (chacks if variables point to the same object in memory)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

#membership operators in, not in
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)



