print(10 > 9)
print(10 == 9)

print("\n", bool("hello"))
print(bool(67))
print(bool(0))

#list of false values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print("\n")

def myfunc():
    return(True)

if myfunc():
    print(67777)
else:
    print(23333)


#isinstance() function

x = (["apple"], ["banana"], ["hotdog"])
print("x is tuple? bzzzzzz:", isinstance(x, tuple))

