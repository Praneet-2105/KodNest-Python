#Adding 2 numbers
def add():
    a,b = 10,10
    c = a+b
    print(c)
add()

#find square of a number
def square():
    a = int(input())
    print(a*a)
square()

#find largest of 3 numbers
def large():
    a,b,c = int(input()),int(input()),int(input())
    if a>b and a>c:
        print(a)
    else:
        if b>c:
            print(b)
        else:
            print(c)
large()

#greet good morning with name
def greet():
    a = input()
    print(f"Good Morning, {a}")
greet()
