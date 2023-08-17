number1 = int(input("Please input some number: "))
num2 = int(input("Please input some number: "))
num3 = int(input("Please input some number: "))

if (number1 <= num2 <= num3) or (num3 <= num2 <= number1):
    print(f"Median is: {num2}")
elif (num2 <= number1 <= num3) or (num3 <= number1 <= num2):
    print(f"Median is: {number1}")
else:
    print(f"Median is: {num3}")

#
text = input("Please input your magic word: ")

if text == text[::-1]:
    print("Congratulations you win. Your word was polindrom")
else:
    print("Try Again Later")

myDict = {1:2, 3:4}

myDict.setdefault()

