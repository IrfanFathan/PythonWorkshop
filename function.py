a=int(input("Enter a random number "))
b=int(input("Enter a"))
print(add(a,b))
subtract(a,b)
print(mult(a,b))
divide(a,b)


def add(a,b):
    s=a+b
    return s
def subtract(a,b):
    s=a-b
    print(s)
def divide(a,b):
    s=a/b
    print(s)
def mult(a,b):
    s=a*b 
    return s           
    