myList = [5, 153, 135, 153, 1, 5665, 156, 1, 566, 8, 1, 16, 86, 681]

index = 0
# number = int(input("Please enter some number: "))
# for i in myList:
#     if number == i:
#         print(index)
#     index = index + 1

# text = "Hello World!"
# for i in text:
#     print(i)

# myDict = {"name": "John", "age" : 33, "lastName": "Smith", "friends" : ["Aram", "Artur", "Varazdat"]}
#
# for key, value in myDict.items():
#     print(f"Key is: {key}, Value is: {value}")
#     if key == "friends":
#         print("Nice to have That much Friends")
#         for name in value:
#             print(f"Hi {name}")
#
# myString = "H"
# print(myString.isupper())
# print(myString.islower())

numbers = list()

i = 0
while i < 10:
    number = (input("Please input some number: "))
    numbers.append(number)
    i += 1

print(numbers)