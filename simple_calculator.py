def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(f"""
Choose your operation :
1. Add
2. Subtract
3. Multiply
4. Divide
""")

choice = int(input("(1/2/3/4): "))
for i in range(choice):
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")
