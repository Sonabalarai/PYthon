import json
from abc import ABC,abstractmethod
from pathlib import Path


# Create database
database = "school_data.json"
data = {"student":[],"teacher":[]}

if Path(database).exists():
    with open(database,'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)   #Its a copy of data
            
def save():
    with open(database,"w") as f :
        json.dump(data,f,indent=4)




class Persons(ABC):
    
    @abstractmethod
    def get_roles(self):
        pass
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def show_details(self):
        pass
    
    @staticmethod
    def validate_email(email):
        if "@"  in email and "." in email:
            return True
        else :
            return False
    
class Student(Persons):
    def get_roles(self):
        return "student"
    def register(self):
        name = input("enter your name:- ")
        age = int(input("enter your age:- "))
        email = input("enter your email:- ")
        roll_no = input("enter your roll number:- ")
        
        if not Persons.validate_email(email):
            print("Invalid email")
            return
        
        for i in data["student"]:
            if i['roll_no']==roll_no:
                print("student already exist")
                return
            
        data['student'].append({
            "name": name,
            "age": age,
            "email":email,
            "roll_no":roll_no,
            "grade":{}
        })
        save()
        print(f"Student {name} registered")  
        
    def show_details(self):
        roll_no = input("enter your roll number:- ")
        for s in data['student']:
            if s['roll_no']==roll_no:
                grade = s['grade']
                avg = sum(grade.values())/len(grade) if grade else 0
                print(f"\n Name : {s['name']}")
                print(f"Roll no : {s['roll_no']}")
                print(f"Grades : {grade}")
                print(f"Average : {avg:.1f}")
                return
            
    def add_grades(self):
        roll_no = input("enter your roll number:- ")
        subject= input("subject:- ")
        marks= float(input("enter your marks:- "))
        
        for i in data['student']:
            if i['roll_no']==roll_no:
                i['grade'][subject] = marks
                save()
                print("garde added successfully")
                return
        print("Student not found !")
            

class Teacher(Persons):
    def get_roles(self):
        return "Teacher"
    
    def register(self):
            name = input("enter your name:- ")
            age = int(input("enter your age:- "))
            email = input("enter your email:- ")
            subject = input("enter your subjects:- ")
            emp_id = input("enter your employee id number:- ")
        
            if not Persons.validate_email(email):
               print("Invalid email")
               return
            for i in data["teacher"]:
                        if i['emp_id']==emp_id:
                            print("student already exist")
                            return
                        
            data['teacher'].append({
                        "name": name,
                        "age": age,
                        "email":email,
                        "subject":subject,
                        "emp_id":emp_id,
                        
            })
            save()
            print(f"teacher {name} registered")
    def show_details(self):
        emp_id = input("enter employee id:- ")
        for t in data['teacher']:
            if t['emp_id']==emp_id:
                print(f"\n Name : {t['name']}")
                print(f"Subject : {t['subject']}")
                print(f" Emp ID: {t['emp_id']}")
        print("Teacher not found !")
            
stud =Student()
tech = Teacher()

print("Press 1 to register a student")
print("Press 2 to register a teacher")
print("Press 3 to add grades")
print("Press 4 to show a student details")
print("Press 5 to show a teacher details")


choice = int(input("enter your choice (1,2,3,4,5) :- "))

if choice==1:
    stud.register()
    
elif choice==2:
    tech.register()
elif choice==3:
    stud.add_grades()
elif choice==4:
    stud.show_details()
elif choice==5:
    tech.show_details()