class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Called init method for People Class")

    def eat(self):
        print(f"{self.name} is Eating....")

    def dance(self):
        print("Dancing....")

    def get_self_information(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")

person1 = People("John", 33)
print(person1.name)
print(person1.age)
person1.dance()
person1.dance()
person1.dance()
person1.dance()
person1.dance()
person1.get_self_information()

# person2 = People()
# person2.name = "Jesica"
# person2.age = 22
# person2.eat()
# person2.get_self_information()
