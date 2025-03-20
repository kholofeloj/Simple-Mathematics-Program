

# 1. Ask the user user to select operation to perform (addition, subtraction, multiplication, division)
operation = input("Select operation to perform: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

# 2. Ask the user user to enter the first number 
num1 = int(input("Enter the first number: "))

# 3. Ask the user user to enter the second number
num2 = int(input("Enter the second number: "))

# 4. Perform the operation selected by the user
if operation == '1':
    result = num1 + num2
    print(f"{num1} + {num2}")
    print(f"The result is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"{num1} - {num2}")
    print(f"The result is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"{num1} * {num2}")
    print(f"The result is: {result}")
elif operation == '4':
    result = num1 / num2
    print(f"{num1} / {num2}")
    print(f"The result is: {result}")
else:
    print("Invalid operation selected")
    exit()