def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)

count(5)

#factorial using function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

# Fibonacci Series
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10)) 