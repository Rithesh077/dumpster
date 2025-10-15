try:
    num_1 = float(input("Enter first number: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()
try:
    num_2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()
operation = input("Enter operation (+, -, *, /, %): ")
if operation == '+':
    result = num_1+num_2
    print(f"{num_1}+{num_2}={result}")
elif operation == '-':
    result = num_1-num_2
    print(f"{num_1}-{num_2}={result}")
elif operation == '*':
    result = num_1*num_2
    print(f"{num_1}*{num_2}={result}")
elif operation == '/':
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num_1/num_2
        print(f"{num_1}/{num_2}={result}")
elif operation == '%':
    if num_2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = num_1 % num_2
        print(f"{num_1}%{num_2}={result}")
