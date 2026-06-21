# GENERATORS
#1  ----- generator that print squares of numbers up to some N -----
def squares(n):
    for i in range(1, n + 1):
        yield i*i

for i in squares(15):
   print(i)


#2  ----- generator that print even numbers between 0 and N inputed by user -----
def evens(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Write your god will number: "))
for i in evens(n):
   print(i)


#3  ----- generator that print numbers divisible by 3 or 4 between 0 and N inputed by user -----
def divisibles(n):
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

n = int(input("Write your god will number: "))
for i in divisibles(n):
   print(i)


#4  ----- generator that print squares of numbers between a and b -----
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

for i in squares(5, 8):
    print(i)



#5  ----- generator that print numbers from N to 0 -----
def reverse(n):
    for i in range(n, -1, -1):
        yield i

for i in reverse(15):
    print(i)


# DATE AND TIME
#1 -----Write a Python program to subtract five days from current date-----
from datetime import datetime, date, timedelta

now = date.today()
five_days_before = now - timedelta(days=5)

print(five_days_before)

#2 -----Write a Python program to print yesterday, today, tomorrow-----
now = date.today()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

print("Yesterday was", yesterday)
print("Today is", now)
print("Tomorrow will be", tomorrow)

#3 -----Write a Python program to drop microseconds from datetime-----
now = datetime.now()
cutted_microseconds = now.strftime("%Y-%m-%d %X")
print(cutted_microseconds)

#4 -----Write a Python program to calculate two date difference in seconds-----
import random

now = datetime.now()
x = random.randint(0, 1000000000)
random_datetime = now + timedelta(seconds=x)

print("Random int is", x)
print("Random datetime is", random_datetime)
print("Difference in seconds is", (random_datetime - now).total_seconds())


# MATH
#1 -----Write a Python program to convert degree to radian-----
import math

angle = int(input("Input degree: "))
print("Output radians:", math.radians(angle))

#2 -----Write a Python program to calculate the area of a trapezoid-----
height = int(input("Height: "))
base1 = int(input("Base 1: "))
base2 = int(input("Base 2: "))
print("Expected area of trapezoid:", (base1 + base2)*height/2)

#3 -----Write a Python program to calculate the area of regular polygon-----
sides = int(input("Number of sides: "))
length = int(input("Lenght of one side: "))
angle = math.radians(360/sides)
unit_area = length*((length/2)*(1/math.tan(angle/2)))/2
print(f"Expected area of regular polygon with {sides} sides and {length} lenght of one side is:", math.floor(unit_area*sides))



#JSON
import os
import json

#getting sample directory
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "sample-data.json")

with open(file_path, "r") as file:
    data = json.load(file)

# Print headers matching the assignment structure
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")















