# Wap to replace all occurence of found number with new number in a given list using function.

def findh(x, h):
	c = 0
	for a in x:
		if (a == h):
			c += 1
	return c

x = [12, 15, 14, 15, 18, 14, 17, 15, 11, 16, 15]
h = 15

print(findh(x, h))
f = input("Enter value to replace : ")
f = int(f)

x[1] = f
x[3] = f
x[7] = f
x[-1] = f
print(x)
