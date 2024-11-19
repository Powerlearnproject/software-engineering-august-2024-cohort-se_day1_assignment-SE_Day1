# Basic Calculator Program
#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))
operator = input('Please enter your ign operator: ')
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1- num2)
elif operator == '*':
    print(num1 * num2)
else:
    print(num1 / num2)