# Function to Add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


print("Please select operation: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")


# Take input from the user
select = int(input("Select operation from 1, 2, 3, 4: "))

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if select == 1:
    print(number_1, "+", number_2, "=")
    print(add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=")
    print(subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=")
    print(multiply(number_1, number_2))

elif select == 3:
    print(number_1, "/", number_2, "=")
    print(divide(number_1, number_2))

else:
    print("Invalid Input")
