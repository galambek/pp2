import os
import re
import json

#getting sample directory
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "raw.txt")

with open(file_path, "r", encoding="utf-8") as file:
    raw = file.read()


# my code
pattern_name = r'\d+\.\n(.+?)\n'
pattern = r'(\d+),000 x (.+?),'

name_matches = re.findall(pattern_name, raw)
matches = re.findall(pattern, raw)

dict = []


for i in name_matches:
    new_dict = {
        "product name" : i
    }
    dict.append(new_dict)
        

z = 0
for num, price in matches:
    temp = ""
    for x in price:
        if x != " ":
            temp += x
        else:
            pass
    dict[z]["price"] = int(temp)
    dict[z]["amount of product"] = int(num)
    z += 1

total_sum = 0
for i in dict:
    total_sum += i["price"] * i["amount of product"]

pattern_time = r'Время: (.*?)\n'

time_match = re.search(pattern_time, raw).group(1)

# pattern_payment = r'Банковская карта: (.*)\n'

# if re.search(pattern_payment, raw):
#     payment_match = re.search(pattern_payment, raw).group(1)



print(json.dumps(dict, indent=4, ensure_ascii=False))
print("Total cost is:", total_sum)
print("Time is:", time_match)
# print("Payment method is:", payment_match)
