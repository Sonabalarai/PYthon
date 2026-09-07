from pathlib import Path
import os
def createfile():
    try:
        name = input("enter your file name:")
        path = Path(name)
        
        if not path.exists():
            with open(path,"w") as f:
                data = input("What you want to write:-")
                f.write(data)
            print("file succcessfully created")
        else :
            print(f"Error file name {name} already exists")
    
    except Exception as err:
        print(f"error named {err} occurred")
            

def readfile():
    try:
        name = input("Enter your file name tha you want to read:-")
        path = Path(name)
        if path.exists():
            with open(path,"r") as f:
                content = f.read()
                print(f"your file content is  \n{content}")
        else:
            print("Your mentioned file name doesnot exist")
    except Exception as err:
        print(f"Error occured as {err}")

def updatefile():
    try:
        name = input("enter your file name:-")
        path = Path(name)
        
        
        
        if path.exists():
        
            print("Operations:")
            
            print("1. Renaming the file name")
            print("2. Adding or appending   content")
            print("3. Over writing the content")
            
            choice = int(input("Enter Your Choice:-"))
            
            if choice ==1:
                newname = input("Enter the new file name:-")
                new_path = Path(newname)
                if not  new_path.exists():
                    path.rename(new_path)
                    print("File renamed successfully")
                else:
                    print("file aready exist")
            elif choice==2:
                with open(path,'a') as f:
                    data = input("Write what you want to append")
                    f.write("\n" + data)
                print("successfully appended")
            elif choice==3:
                with open(path,"w") as f:
                    data = input("Write what you want to overwrite with")
                    f.write(data)
                print("Successfully over written")
        else:
            print("Given file name doesnot exist")
    except Exception as err:
        print(f"error occurred as {err}")
                
def deletefile():
    try:
        name = input( " please tell your file name:-")
        path = Path(name)
        
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("Given file name doesnot exist")
    except Exception as err:
        print(f"The error occurred as {err}")




print("You press 1 to create a file")
print("You press 2 to read  a file")
print("You press 3 to update a file")
print("You press 4 to delete a file")

a = int(input( "\nenter your number choice:"))

if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    updatefile()
if a==4:
    deletefile()
    


