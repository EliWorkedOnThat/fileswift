#OOP
#Object
class car:
    def __init__(self, model , year , color ,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
#Method
    def drive(self):
        print(f"{self.model} is driving.. Vroom")

    def stop(self):
        print(f"You stopped the {self.model}")

    def change_gear(self):
        print("Changing gears")

#Outputs
car1 = car("Lexus",2024 , "Red", False)
car2 = car("Toyota" , 2023 , "Blue" , True)
car3 = car("Lexus", 2020 , "Yellow" , False)

car1.drive()
car1.stop()
car1.change_gear()

car2.drive()
car2.stop()

car3.drive()
car3.stop()

print(car1.model)
print(car2.model)
print(car3.model)











