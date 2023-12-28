"""
Tuple:
        It is immutable.(means it can not suppoprt to change in it.)
 
IT IS STORED IN ROUND BRACKET (). IT IS NOT COMPULSORY TO USE.
"""

marks = (95, 98, 97, 97, 97)

print(marks.count(97))        #To find no. of value store in it.

print(marks.index(97))        #To find first index value of given value.

#Trick to store value in tuple.
y = (96,)
marks += y
print(marks)
