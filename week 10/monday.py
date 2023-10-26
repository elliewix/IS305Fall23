

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1:
        return fib(x - 1) + fib(x - 2)
    else:
        print("bad input")

print(fib(0))

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(30))