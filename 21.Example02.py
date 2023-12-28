# WAP to calculate the factorial of a given number.

x = input("Enter number : ")
x = int(x)

i = 1
h = 1
while(i <= x):
    h = i * h
    i += 1

print(int(h))

# WAP to find no. of trailing zeroes in that factorial

a = 1
while(True):
    b = 10 ** a
    if(h % b == 0):
        a += 1

    else:
        print(int(a - 1))
        break
