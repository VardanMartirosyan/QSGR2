class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def change_transmission(self, transmission):
        if transmission == "D":
            print("Turned On Drive Mode")
        elif transmission == "R":
            print("Turned On Reverse Mode")
        elif transmission == "N":
            print("Turned On Neutral Mode")
        elif transmission == "P":
            print("Turned On Parking Mode")
        else:
            print("PLEASE DONT DRIVE")

    def set_millage(self, millage):
        self.millage = millage

    def get_millage(self):
        return self.millage

    def lock_doors(self):
        print(f"{self.make} doors locked")

    def unlock_dors(self):
        print(f"{self.make} doors unlocked")



car1 = Car("Lada", "Niva")
car1.set_millage(100000)
car1.change_transmission("R")
car1.change_transmission("N")
car1.change_transmission("D")
car1.change_transmission("P")
car1.change_transmission("A")
car1.lock_doors()
car1.unlock_dors()
print(car1.get_millage())
