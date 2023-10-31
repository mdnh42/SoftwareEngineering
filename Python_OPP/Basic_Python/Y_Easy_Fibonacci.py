

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


x = int(input())

for i in range(1, x+1):
    print(fib(i), end=" ")
    
    