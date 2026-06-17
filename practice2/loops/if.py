#code works from top to bottom and stops when 1 condition is satisfied
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")

#shorthand if else (including assigning value to variable)
bigger = a if a > b else b

#shorthand if else if
print("cheremsha") if a < b else print("chereshnya") if b == a else print("abobus")

#match statement
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:                                        #_ is default case(when no other condition is true)
    print("Looking forward to the Weekend")
    