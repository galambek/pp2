def fibonachi(n):
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

a = int(input("Enter number of sequnce elements: "))
gen = fibonachi(a)
for x in range(a):
    print(next(gen))
