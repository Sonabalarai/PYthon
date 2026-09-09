# Class is a blue print of an object
# Object is an instance of class

# class Car:
#     name="Toyota"
    
#     def details(self):
#         print("This a the toyota Car")

# c = Car()
# print(c.name)
# print(c.details())


# Constructor is a special type of method that is automatically initialized when function
# is called
# constructor method self will help to capture the location of an object so that we will be
# able to create multiple object of a single class

# class Animals:
    
#     def __init__(self,weight,age):
#         self.weight = weight
#         self.age = age
    
# tiger = Animals(200,60)
# cat =Animals(10,10)

# print(tiger.weight)
# print(cat.age)


# TYpes of methods : There are 3 types of methods
# 1)instance/object method -> captures or target the location of object
# 2)class method-> target or capture the location of class
# 3)static method->It doesnot target any location

# 
class Animal:
    a= 19
    
    def __init__(self,name):
        self.name = name
    
    def hello(self): # instance method
        print(f"this instance mehtod {self.name}")
        
    @classmethod
    def details(cls):
        print(f"this class method {cls.name}")

    @staticmethod
    def speak():
        print("Iam a static method")
        
obj = Animal("lion")
# obj.details()
# print(obj.details())
print(obj.speak)
