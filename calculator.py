def add (a,b):
    result = a+b
    print(result)

def sub(a,b):
    result = a-b
    print(result)

def mult(a,b):
    result = a*b
    print(result)

def div(a,b):
    result = a/b
    print(result)

a = int(input("Enter your first numer: "))
b = int(input("Enter your second numer: "))
op = input("Enter the operator")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mult(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid operation")