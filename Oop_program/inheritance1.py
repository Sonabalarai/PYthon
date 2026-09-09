# class Animal:
#     a= 19
#     print("this is animal class")
    
#     def __init__(self,name):
#         self.name = name
#     def details(self):
#         print("he a doctor")
        
# class Cat(Animal):
#     print("this is a child class")
    
# a = Animal("tom")
# c=Cat("teke")
# c.details()
# print(a.name)


# Inheritence vitra constructor
#  single inheritance
# class BagFactory:
#      def __init__(self,materials,zips,pocket):
#          self.materials = materials
#          self.zips = zips
#          self.pocket = pocket
         
#      def details(self):
#          print("your bag details are:")
#          print(self.materials)
#          print(self.zips)
#          print(self.pocket)
         
# class Reebok(BagFactory):
#     def __init__(self, materials, zips, pocket,color):
#         super().__init__(materials, zips, pocket)
#         self.color = color
        
#         def details(self):
#             print(self.color)
#             print(f"the color of bag is {self.color}")
#             return super().details()
        
# bag1 = BagFactory("leather",3,2)
# bag2 = Reebok("polyster",4,2,"Red")
        
# bag1.details()
# bag2.details() 


# @2Polymorphism
# To get the polymarphism concept we have two ways 1)method overriding and 2)metho overloading
# Method overriding is the sitution where parent and child class has the same method name 
# and while call that same named method with object of child class then at that time the method
# of child class will override the method of parent class

# class Animal:
#     a=10
#     def __init__(self,name):
#         self.name = name
        
#     def hello(self):
#         print("Hello every one")
        
#     def speak(self):
#         print("animals cannot speak")
# class Human(Animal):
#     b=20
#     def __init__(self, name):
#         super().__init__(name)
#     def speak(self):
#         print("Human cannot speak")
        
# h = Human("cat")

# print(h.a)
# h.speak()
# h.hello()

# Method loading is not accepted in python programming language but in other programing language 
# like c++,java

# Method overloading is a concept wher same name method is created or can exists within a same
# class name but with the different parameters and while calling them they behaves differently

# class Animal:
#     a= 23
#     def speak(self,name):
#         print(f"the animal {self.name} cannot speak")
        
#     def speak(self,name,age):
#         print(f"This animal name is {self.name} and age is {self.age}")
        
# @3 Encapsulation

# class Factory:
#     name= "Toyota" #publi class attribute can be accessed from any where
#     _brand = "F9-1z"  # protected access modifier but donot work in python , but it is written to 
#     # tell other developer it is protected where this  same code is to run just in case in java, c++
#     # for protected use single underscore(_)
#     def __init__(self,age):
#         self.__age = age   # double underscore is for private which cannot be access except where it has been define
    
#     def details(self):
#         print(f"your car is {self.name}")
        
# f = Factory(5)  
# # print(f.age)   # since it is private so cannot be accessed
# f.details()  
# print(f._brand)


# @4 Abstraction => It doesnot exist in python but can be achieved by using python "abc" library
# from abc import ABC, abstractmethod

# class Factory(ABC):
#     @abstractmethod
#     def enginestart():
#         pass
    
    
# class car(Factory):
#     def enginestart(self):
#         print("this is car")


# class truck:
#     print("This is truck")

# c= car()
# c.enginestart()
# t= truck()