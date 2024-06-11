#2 Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.
# age = int(input('How old are you? '))
# print()
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old')
# print(f'In 20 years, you will be {age + 20} years old')
# print(f'In 30 years, you will be {age + 30} years old')
# print(f'In 40 years, you will be {age + 40} years old')

age = int(input('How old are you? '))
print()
print(f'You are {age} years old. ')
for future in range(10, 50, 10):
    print(f'In {future} years, you will be {age + future} years old')

#3 Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1


for element in my_list: 
    print(element)


#4 Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

index = 0
while index < len(my_list):
     number = my_list[index]
     if number % 2 == 0:
         print(number)
     index += 1

for number in my_list:
    if number % 2 != 0:
        print(number)

#5 Print all of the even numbers in the following list of nested lists. Don't use any while loops.


for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)

#6  In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(nested_list)

#7 Write a find_integers function that returns a list of all the integers from my_tuple:
def find_integers(things):
    return   [ element 
              for element in things
              if type(element) is int ]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

#8 Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0  }

print(result)

#9 Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:


def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number
    
    return result
   
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

