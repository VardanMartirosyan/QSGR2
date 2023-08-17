# def congrats(name, gender="male"):
#     if gender == "male":
#         print(f"{name} is Man")
#     elif gender == "fmale":
#         print(f"{name} is Woman")
#     else:
#         print("Next time make sure that your gender is attached correct way, male or fmail")
#     print(f"Congrats {name}")
#     print("Welcome to our Class")


# userName = input("Please enter your name: ")
# userGender = input("Please input your gender: ")
# congrats("Liana", "fmale")
# congrats(userName, userGender)
# congrats("Johan")

# print("Hello", "Wold", sep=",", end=" ")
# print("Hi")
# variable = congrats("John")
# print(variable)

# def summ(num1, num2):
#     return num1 + num2
    # result = num1 + num2
    # return result

# num1 = 10
# num2 = 20
# num3 = summ(num1, num2)
# print(num3)
# print(summ())

############################################
def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input("Please input some number: "))
result = is_even_number(number)
print(result)
print(is_even_number(13))