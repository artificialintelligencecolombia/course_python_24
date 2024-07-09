# 1. We can initialize a empty class by using 'pass'
class User():
    pass

user_1 = User()
# print(user_1) # <__main__.User object at 0x000002ACC65777D0>

# 2. When the object is initilized, we can set the variables to their starting values. For this, we use the constructor. It allows functions as well to being automatically executed.
class Car():
    # constructor
    def __init__(self, seats): # self is the actual object being initialized. The arguments are required to initialize the object.
        # we can add unlimited parameters to the constructor
        self.seats = seats # the object's attr are 'self.attr'
        self.kms = 0 # We can provide default values for attrs.
my_car = Car(5)
# print(my_car.seats) # 5
# print(my_car.kms) # 0


# 3. Methods 
class UsrAccount():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.following = 0
        self.followers = 0
        
    def follow(self, user): #self is required in every method.
        self.following += 1
        self.followers += 1

# obj creation        
usr_2 = UsrAccount("my_ig_account", "1234")

# method call
usr_2.follow(user_1)
print(usr_2.followers) # 1

usr_2.follow("another_user")
print(usr_2.followers) # 2       
