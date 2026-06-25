import re

def match_strings(text):

    # pattern = r'ab*'
    # pattern = r'ab{2,3}(?!b)'
    pattern = r'[a-z]+_[a-z]+'

    if re.match(pattern, text):
        print(f"'{text}': Matches")
    else:
        print(f"'{text}': Not at all(((")


# Test cases
test_strings = ["a", "ab", "abbb", "abbbb", "abbc", "ba", "sabbc", "abbbc"]

for i in test_strings:
    match_strings(i)




