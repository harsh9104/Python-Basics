# WAP which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard.

sum = 0
while(True):
    print("print 'q' for quit billing")
    x = input("Enter product ammount : ")
    if(x != 'q'):
        sum = sum + int(x)
        print(f"Your Bill Total so far : {sum}")         # used f string : print(f"xyz{variable}").

    else:
        print(f"\n Your Bill Total is : {sum}.\n Thank you for shopping! \n")
        break
