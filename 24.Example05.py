# write a program to create calculator using function.

def Calculator(a, b, op):

    if(op == "*"):
        print(a*b)
    elif(op == "+"):
        print(a+b)
    elif(op == "-"):
        print(a-b)
    elif(op == "/"):
        print(a/b)
    else:
        print("Eror 404")

c = input("Enter first number : " + "")
d = input("Enter second number : " + "")
o = input("Enter operator : " + "")
 
c = int(c)
d = int(d)

Calculator(c, d, o)
