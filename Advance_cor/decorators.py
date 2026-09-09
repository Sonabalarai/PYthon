#1 Decorator wraps a functions to add extra feature without modifying its code

# def extrarequirement(func):
#     def wrapper():
#         print("Hello , this is from NYC team")
#         func()
#         print("Than you , visit again!")
#     return wrapper
 
# @extrarequirement       
# def greeting():
#     print("good morning")
    
# greeting()


#2 *args and ** kwargs
# when you don't know how many arguments a function will receive, use *args (for positional) 
# args hold the tuple
# use **kwargs for keyword

# def addition(*args):
#     s=0
#     for i in args:
#         s= s+i
#     return s
# print(addition(2,9,8,9))


##  this **kwargs uses = when  you are asked to take information about something and the user can give
# any thing and any number of information so at taht time we developwes can write **kwargs which 
# make the info to dictionary



# def extrarequirement(func):
#     def wrapper(**kwargs):
#         print("Hello , this is from NYC team")
#         func(**kwargs)
#         print("Than you , visit again!")
#     return wrapper

# @extrarequirement
# def info(**kwargs):
#     return kwargs.keys()

# print(info(name="sona",age=27, profession ="AI engineer"))