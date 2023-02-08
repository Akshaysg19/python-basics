def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Lets Begin:")
print("click 1 for add, 2 for Subtract,3 for Multiply and 4 for devision")

while True:
    choice = input("Enter the choice : ")

    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter the 1st Number : "))
            num2 = float(input("Enter the 2nd Number : "))
        except ValueError:
            print('Invalid Input, Please Enter the proper Number')
            continue

        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(sub(num1,num2))
        elif choice == '3':
            print(mul(num1,num2))
        elif choice == '4':
            print(div(num1,num2))
    else:
        print('Invalid Input')