def add(a,b):
    return a+b

def substract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b

def calculator(a,b):
    return add(a,b),substract(a,b),divide(a,b),multiply(a,b)

while True:
    choice = input("Do u want to do calculation?yes/no:").lower()
    if choice == "no":
        print("Thank You")
        break
    else:
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        output = calculator(a,b)
        print("Addition",output[0])
        print("Substraction",output[1])
        print("Division",output[2])
        print("Multiply",output[3])