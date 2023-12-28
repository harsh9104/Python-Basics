marks = [95, 97, 98]

#for loop
for score in marks:
    print(score)

#While loop
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

#different operations

marks.append(96)           #Append is use to add any value in list at the end.
print(marks)

marks.insert(0, 99)        #insert is use to add any value in list at any index value.
print(marks)

marks[1] = 90             # use to replace any value at any index.

print(96 in marks)         #In keyword is use to find value in list and gives value in Boolean form.

print(len(marks))          #It is use to measure length of the given list. 

marks.clear()              #It is use to clear(Empty) any list. 
print(marks)
