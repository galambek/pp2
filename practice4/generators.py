#yield in def is what makes a function generator. it is return but it doesnt terminate function, just pauses it
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)



def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))



def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(gen)       #prints: <generator object simple_gen at 0x0000026745B25D20>
print(next(gen))
print(next(gen))
print(next(gen))

#fibonacchi numbers
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 12 Fibonacci numbers
gen = fibonacci()
for x in range(12):
  print(next(gen))

#send() function
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
print(next(gen)) # Prime the generator
gen.send("Hello")
gen.send("World")


#close() function
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()