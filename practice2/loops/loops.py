
#while loop with break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("\n")

#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement when cycle stops
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
else:
  print("i is 3 now")  #as we see, it doesn't work with break


#for loop is used as iteration through sequences(even strings)
fruits = ["apple", "banan", "dragonfruit", "pineapple"]
for x in fruits:
  print(x)
else:
  print("just checking")

#range(x) - means from 0 to x-1
#range(x, y) - means from x to y-1 (or to y+1 depending on step sign)
#range(x, y, z) - same but with z step
for x in range(3, 1, -1):
  print(x)

