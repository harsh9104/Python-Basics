a = input("Enter first number : ")
op = input("Enter operator(+,-,*,/,%) : ")
b = input("Enter second number : ")

a = int(a)
b = int(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    #print(int(a / b))
    print(a / b)
elif op == "%":
    #print(int(a % b))
    print(a % b)
else:
    print("Invalid Operation.")
