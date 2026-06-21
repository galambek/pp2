import math

# Constants
print(math.pi)        # 3.141592653589793
print(math.e)         # 2.718281828459045

# Numbers rounding
print(math.ceil(4.2))   # Rounding to the nearest up value -> 5
print(math.floor(4.8))  # nearest down -> 4
print(math.trunc(4.9))  # Drops numbers after floating point -> 4

# Power and square root
print(math.pow(2, 3))   # 8.0 (always return float)
print(math.sqrt(16))    # 4.0

# Factorial and GCD
print(math.factorial(5)) # 120
print(math.gcd(24, 36))  # 12

# Trigonometry (arguments are accepted in rads)
angle = math.radians(90) # from degrees to rads
print(math.sin(angle))   # 1.0