try:
    def mon(x):
        if x == 1:
            print("January")
        elif x == 2:
            print("Feburary")
        elif x == 3:
            print("March")
        elif x == 4:
            print("April")
        elif x == 5:
            print("May")
        elif x == 6:
            print("June")
        elif x == 7:
            print("July")
        elif x == 8:
            print("August")
        elif x == 9:
            print("September")
        elif x == 10:
            print("October")
        elif x == 11:
            print("November")
        else:
            print("December")
    x=int(input("enter a number from 1 to 12: "))
    mon(x)
except ValueError:
    print("That is not a number")
if x > 12 or x < 1:
    print("That is not a number between 1 and 12")
else:
    pass