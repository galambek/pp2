#lambda is a small fuction that can accept any num of arguments and which can be assigned to some variable, so that variable becomes function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#mydoubler becomes lambda specified in myfunc()
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#map(lambda function, iterable with items to be sent as arguments to lambda)
numbers = [1, 2, 3, 4, 5]
doubler = list(map(lambda x: x**2, numbers))
print(doubler)

#filter(lambda which can return true/false, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#sorted(iterable, lambda that returns key based on which sorting happens)
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: len(x[0]))
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
