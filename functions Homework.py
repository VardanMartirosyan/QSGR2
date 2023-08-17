# 1. Write a function to multiply all the numbers in a given list
import math


def multiply_all_elements_from_list(someList):
    result = 1
    for i in someList:
        result *= i

    return result


myList = [-10, 1, 2, 3, 4, 5]
print(multiply_all_elements_from_list(myList))
n = 100
abs(n - 50)
# 2. Write a function that takes a list and returns a new list with unique elements of the first list

# def return_list_without_duplicates(someList):
#     resultList = []
#     for i in someList:
#         if not someList.count(i) > 1:
#             resultList.append(i)
#
#     return resultList
#
#
# myList = [1, 2, 2, 3, 4, 2, 1, 5, 4]
# print(return_list_without_duplicates(myList))

# 3. Write a function to print the even numbers from a given list.
# def get_even_numbers_from_list(someList):
#     for i in someList:
#         if i % 2 == 0:
#             print(i, end=" ")
#
#     print()
#
# myList = [1, 2, 2, 3, 4, 2, 1, 5, 4]
# get_even_numbers_from_list(myList)

# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#      Sample String : 'The quick Brow Fox'
#      Expected Output :
#      No. of Upper case characters : 3
#      No. of Lower case Characters : 12

# def count_of_upper_and_lower_cases(text):
#     upperCaseCount = 0
#     lowerCaseCount = 0
#     for i in text:
#         if i.isupper():
#             upperCaseCount += 1
#         elif i.islower():
#             lowerCaseCount += 1
#
#     print(f"Upper Case count is: {upperCaseCount}")
#     print(f"Lowe Case count is: {lowerCaseCount}")
#
# count_of_upper_and_lower_cases("Hello World")
# print(" ".isalpha())


# 5. Write a Python function that takes a number as a parameter and check the number is prime or not

def is_prime(number):
    if number <= 0 or number == 4:
        return False
    for i in range(2, math.ceil(number**(1/2))):
        if number % i == 0:
            return False

    return True


number = int(input("Please input some number: "))
print(is_prime(number))
