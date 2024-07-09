# Inheritance allows one class to inherit attrs and methods from another class.
# Its for code reuse.

# PARENT CLASS
class Animal():
    # Constructor method takes a name parameter and initializes the name attribute and num_eyes attribute.
    def __init__(self, name):
        self.name = name # I have to provide the 'name' parameter when creating the instance.
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, Exhale.")
    
    def info(self):
        print(f"I am a {self.name}")
        
# Creating an instance of Animal
dog = Animal("dog")
dog.breathe() # Output: Inhale, Exhale.
dog.info() # Output: I am a Dog

# CHILD CLASS
# The Fish class inherits from the Animal class.
class Fish(Animal):
    def __init__(self, name):
        # Inherit attributes
        # Call the constructor of the parent class and pass the name parameter
        super().__init__(name)
    
    # Child class can contain unique methods/attrs.
    def swim(self):
        print("Swimming in sea")
    
    # Inherit methods (and modify them)
    def breathe(self):
        super().breathe()
        print("underwater.")
    
        
nemo = Fish("fish")
nemo.breathe()  # Output: Inhale, Exhale. -> underwater.
nemo.info()  # Output: I am a Fish
nemo.swim()  # Output: Swimming in the sea

# ORDER

# 1. The name parameter is received by the child class's __init__ method.
# 2. The child class calls super().__init__(name) to pass the name parameter to the parent class.
# 3. The parent class's __init__ method executes, initializing the name attribute and any other attributes defined in the parent class.