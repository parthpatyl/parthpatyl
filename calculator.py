def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Syntax Error"

print("[-----Simple Calculator-----]")

while True:
    print("\n Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Subtract")
    print("4. Divide")
    print("5. Exit")
    
    select = input("Enter Operation: ")

    if select == '5':
        print("Exiting the calculator...")
        break

    num1 = float(input("Enter first Value: "))
    num2 = float(input("Enter Second Value: "))

    if select=='1' :
        print("Answer = ",add(num1,num2))
    elif select=='2' :
        print("Answer = ",subtract(num1,num2))
    elif select=='3' :
        print("Answer = ",multiply(num1,num2))
    elif select=='4' :
        print("Answer = ",divide(num1,num2))
    else:
        print("Invalid Input")