
# 1) Function to add two numbers
def add(a, b):
    return a + b


# 2) Function to subtract two numbers
def subtract(a, b):
    return a - b


# 3) Function to multiply two numbers
def multiply(a, b):
    return a * b


# 4) Function to divide two numbers
def divide(a, b):
    return a / b


# 5) Take two integer inputs from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


# 6) Call each function and print the results
print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))

if num2 != 0:
    print("Quotient:", divide(num1, num2))
else:
    print("Quotient: Cannot divide by zero!")
