# Importing the math module
import math

# Prompting the user for input
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Prompting the user for the operation
operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# Performing arithmetic operations based on the user's choice
if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    result = number_1 / number_2
else:
    print("Invalid operation. Please try again.")
    exit()

# Prompting the user for notes
notes = input("Enter your notes: ")

# Displaying the results
print(f"The result of {number_1} {operation} {number_2} is {result}.")
print(f"Notes: {notes}")
6