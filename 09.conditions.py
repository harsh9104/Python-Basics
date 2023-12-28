"""
if
elif  => else if
else

~there are no curly brackets for condition start and end
~in Python there is a 4 space leave defind that the given statement is use for upper condition.
"""
age = input("Enter your age : ")

age = int(age)

if age >= 18:
    print("You are adult.")
    print("You can vote.")

elif age < 5:
    print("You are child.")

else:
    print("You are in school.")

print("Thank You!")  #This statement print everytime
