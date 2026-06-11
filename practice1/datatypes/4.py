#f-strings(formatting)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#placeholder including modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#placeholder including math operations
txt = f"The price is {20 * 59} dollars"
print(txt)

#escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "We are the so-called \n\"Vikings\" \nfrom the north."
print(txt)
