
def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
try:
    print("Chose to: ")
    print("1. Multiply")
    print("2. Divide")
    print("3. Subtract")
    print("4. Add")
    ch=int(input("Chose one and write the number here: "))
    num=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    if ch==1:
        print(num,"multiplied by",num2,"is",multiply(num,num2))
    elif ch==2:
        print(num,"divided by",num2,"is",divide(num,num2))
    elif ch==3:
        print(num,"subtracted by",num2,"is",subtract(num,num2))
    elif ch==4:
        print(num,"add",num2,"is",add(num,num2))
except ValueError:
    print("This is not a number.")
except ZeroDivisionError:
    print("You can't divide a number with 0.")