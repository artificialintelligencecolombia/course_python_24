# A class is a blunde of data and functionality. a class creates a object.
class Person():
    # init method initializes object's attrs with specific values whe the obj is created.
    def __init__(self, name, age, gender):
        self.person_name = name
        self.person_age = age
        self.person_gender = gender
    
    def greet(self):
        print(f"Hello, my name is {self.person_name}")
        
person1 = Person("Bot1",1,"femenine")

person1.greet()
print(f"Message: {person1.person_name} age is: {person1.person_age}")

bot_age = person1.person_age
print(type(bot_age))