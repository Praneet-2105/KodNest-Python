def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)

# add(10,20) --> Error because in python overloading is not supported
add(10,20,30) #60 

def add(a,b=0,c=0):
    print(a+b+c)

add(10,20)
add(10,20,30)
add(10)

# args 0 - n arguments are passed --> tuple
def add(*a):
    #print(a)
    print(sum(a))

add(10,20)
add(10,20,30)
add()
add(10,20,30,40,50)