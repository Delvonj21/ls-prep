# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(num1, num2):
    return num1 * num2


first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))
product = multiply(first_num, second_num)
print(f'{first_num} * {second_num} = {product}')












