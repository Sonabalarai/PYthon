import random
# print("helo guys")

# a ="Hello how are you"
# print(a[5:9])
# print(a[9:13])
# print(a[13:17])

# n1 = int(input("enter the 1st number: "))
# n2 = int(input("enter the 1st number: "))

# if n1>n2:
#     print(n1)
# else : 
#     print(n2)

# gender = input("enter the your gender: ")

# if gender == "M" or gender=="m" or gender=="Male" or gender=="male":
#     print("Hello Good morning sir")
# elif gender=='F' or gender=='f' or gender=='Female' or gender=='female':
#     print("goo morning mam")
# else :
#     print("good morning sir or madam")

# num = int(input("enter the number: "))

# if num%2==0:
#     print("even")
# else :
#     print("odd")

# year = int(input("enter your year: "))

# if year%100==0 and year % 400 ==0: #centure n leap year
#     print(f" {year} is a leap year")
# elif year%100!=0 and year % 4==0 : #normal year
#     print(f"{year} is  a leap year")
# else:
#     print("not a leap year")

#multiplication of 5
 
# for i in range(1,11):
#     print(f"5 * {i}","=",i*5)

# num = int(input("enter your number:-"))
# for i in range(num,0,-1):
#     print(i)

# n= int(input("enter your number;-"))

# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n = int(input("enter your number:-"))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else :
#         odd+=i        
# print(even, odd)

# n = int(input("enter your number:-"))
# count=0
# p_sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         p_sum+=i
#         count+=1
# if count==2:
#     print(f"{n} is a prime number")
# else :
#     print(f"{n} is not a prime number")

# str = "Python"
# rev = ""
# # print(str[-1: : -1])
# for i in range(len(str)-1,-1,-1):
#     rev = rev + str[i]
# print(rev)

# a = "ABc"
# rev1 =""
# # rev2 =""

# for i in range(len(a)-1,-1,-1):
#     rev1=rev1 + a[i]
# # for i in range(len(a)-1,-1,-1):
# #     rev2 = rev2+ a[i]
# if rev1==a:
#     print(f"{a} is a pallindrome string")
# else :
#     print(f"{a} is not a pallindrome string")
    
# print(rev1,rev2)


val ="12837jsnfslido%^un&&"
digit= 0
char = 0
spchar =0

# for i in val:
#     if i.isdigit():
#         dihgit+=1
#     elif i.isalpha():
#         char+=1
#     else :
#         spchar+=1
# print(char)
# print(spchar)
# print(dihgit)

# print(ord("A"),ord("Z"))
# print(ord("a"),ord("z"))
# print(ord("0"),ord("9"))

# for i in val:
#     if (ord(i) >=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         char+=1
#     elif ord(i)>=48 and ord(i)<=57 :
#         digit+=1
#     else:
#         spchar+=1
# print(f"characters - {char} , digits - {digit}, special character - {spchar}")        

# a=1243
# a = str(a)
# for i in range(0,len(a),1):
    
#     print(a[i])

# QQQ

# a = int(input("enter your number:"))
# r=0
# while a != 0:
#     rem=a%10
#     print(rem)
#     a=a//10
 
# PRINT IN REVERSE ORDER   
# a = int(input("enter your number:"))
# r=0
# while a != 0:
#     r=r*10+a%10
#     print(r)
#     a=a//10    

# com = random.randint(1,100)

# tries = 0

# while True:
#     tries +=1
#     hum= int(input("enter your guess:-"))
    
#     if hum==com :
#         print("Conguralation you have won the game!")
#         break
#     elif hum>com:
#         print("you have guess higher value , please go for lower value !")
#     elif hum<com:
#         print("you have guess lower value so please go for litter higher value !")
#     else:
#         print("your out of range")
# print(f"Completed in {tries} tries")

choices =["rock","scissor","paper"]
com = random.choice(choices)


while True:
    player = input("enter your guess among [rock or scissor or paper] :- ")
    
    if player =="quit":
        print("thank for your time")
        break
    
    if com == player:
        print("Draw game, please guess next")
    elif (com == "rock" and player =="scissor") or (com=="paper" and player=="rock") or(com=="scissor" and player=="paper"):
        print("you lose the game. You can play again")
        
    elif (com =="paper" and player=="scissor") or (com=="scissor" and player=="rock") or (com=="rock" and player=="paper"):
        print("you won the game .Conguratulation !")
        break
    else:
        print("Invalid ! guess the possible choice !")
        
# Add

def add(a,b):
    print(a+b)
    
print(add(10,12))
        
    