#1
def mygen(n):
    a = 0
    while True:
        if a <= n:
            yield a*a
            a += 1
        else:
            raise StopIteration

        

gen = mygen(15)
print(next(gen))
print(next(gen))
print(next(gen))

#while True:
#    print(next(gen))

#2
def even(n):
    a = 0
    while True:
        if a <= n and a % 2 == 0:
            yield a
            a += 2
        else:
            raise StopIteration


a = input("Write your number: ")
gen = even(int(a))
print(next(gen))
print(next(gen))
print(next(gen))

#3
def cheremsha(n):
    a = 0
    while True:
        if a <= n:
            if a % 3 == 0 or a % 4 == 0:
                yield a
                a += 1
            else:
                a += 1
        else:
            raise StopIteration
        

a = input("Write your number: ")
gen = cheremsha(int(a))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))