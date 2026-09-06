# Function 
# def add(a,b,c):
#     print(a+b)
    
# add(29,10)

# Argument type are of three type

# 1)Positional argument
# above example is positional argument  thAT is well we pass the argument

# lis= ["fruit","appla"]
# print(lis)
# l=list(lis[1])
# l[4]="e"
# lis1="".join(l)
# lis[1]=lis1
# print(lis)
# print(l)

num=[1,2,5,72,3,5,2,2]

# seen = set()
# final_list=[]
# for i in num:
#     if i in seen:
#         if i not in final_list:
#             final_list.append(i)
#     else:
#         seen.add(i)
        
# print(final_list) 


# Q find the largest value from list and return its index as well
# n = [12,89,-10,26,40,100]
# large = n[0]
# a=0
# for i in n:
#     if i>large:
#         large = i
#         a=n.index(i)
        
        
# print(large,a)

#Q find the second largest value in the list

# a =[12,89,90,1000,23,999]

# large = a[0]
# sec_large = a[0]

# for i in a:
#     if i > large:
#         sec_large=large
#         large = i
#     elif i>sec_large:
#         sec_large=i
        
# print(f"The largest number is {large} and second largest number is {sec_large}" )


# Q is the list is already sorted check

# a= [2,57,1,0,8]
# a=[1,2,3,4]

# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")



# QTuple 
# def pack_unpack():
#     return "sona",27,"sona@gmail.com"  


# info = pack_unpack()
# # unpack 
# name, age, email = info
# print(info)
# print(name)
# print(age)
# print(email)


tup = (1,2,"sona",80,3,3,1,"sona")

# print(tup.index(2))

# print(tup.count(3))
# a,b,c,d,e=0,0,0,0,0
# rep=[]
# for i in range(0,len(tup)-1):
    
#     if tup.count(tup[i])>1:
#         rep.append(tup[i])
    

# s=set(rep)

# print(list(s))

# print(type(l)) 

# Q merge two dictionaries

# d1 ={"a":10,"b":20,"c":30}
# d2 = {"d":10,"e":20,"f":30}

# # d1.update(d2)
# # print(d1)

# for i in d2:
#     d1[i] =d2[i]
# print(d1)


#Q   SUM

# d1 ={"a":10,"b":20,"c":30}

# sum = 0
# for i in d1:
#     sum+=d1[i]
    
# print(sum)

# Q2 count the frequency of each element in a list using a dicionary

# l = ["a","b","a","c","b","a"]
# d={}

# for i in l:
#     if i in d:
#         d[i]+=1
        
#     else :
#         d[i]=1
# print(d)


# Q
# d1 ={"a":10,"b":20,"c":30}
# d2 = {"c":30,"d":40,"e":50}

# for i in d2:
#     if i in d1:
#         d1[i] +=d2[i]
#     else:
#         d1[i]=d2[i]
        
# print(d1)

# Q)Try , exception handling, else, finally

# n1=20
# n2 = 2

# try:
#     print(n1/n2)
# except Exception as err:
#     print(f"Sorry we got an error {err}")
    
# else:
#     print("no error")
    
# finally:
#     print("If there is error or no errr i will run always")
    

# Try , exception , raise=>make or throw your wn custom error

age=int(input("enter your age:-"))

if age<18:
    raise TypeError("you are not eligible for voting")

print("you are eligible")


    

