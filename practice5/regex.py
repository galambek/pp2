import re

#Matching
def match_strings(text):
    # r'ab*'             match
    # r'ab{2,3}(?!b)'    match
    # r'[a-z]+_[a-z]+'   findall
    # r'[A-Z][a-z]+'     findall
    # r'^a.*b$'          match


#Replacement
def replace(text):
    return re.sub(r'[ ,.]', ':', text)    #simple replacement
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)  #snake to camel
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)   #inserting spaces before capitals
    return (re.sub(r'(?<!^)(?=[A-Z])', '_', text)).lower()   #camel to snake

#Splitting
def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)








