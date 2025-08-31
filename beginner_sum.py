# Enhanced Calculator
# Performs multiple operations on two numbers

print("=== Enhanced Calculator ===")
print("Enter two numbers to perform multiple operations")

# Get input from user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f"\nResults for {number1} and {number2}:")
print("-" * 30)

# Addition
addition = number1 + number2
print(f"Addition: {number1} + {number2} = {addition}")

# Subtraction
subtraction = number1 - number2
print(f"Subtraction: {number1} - {number2} = {subtraction}")

# Multiplication
multiplication = number1 * number2
print(f"Multiplication: {number1} × {number2} = {multiplication}")

# Division (with error handling for division by zero)
if number2 != 0:
    division = number1 / number2
    print(f"Division: {number1} ÷ {number2} = {division:.2f}")
else:
    print(f"Division: {number1} ÷ {number2} = Cannot divide by zero!")

print("-" * 30)
print("All operations completed!")
