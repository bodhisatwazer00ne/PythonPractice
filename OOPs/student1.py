import re

class Student:
    def __init__(self,name,house,marks):
       if not name:
           raise ValueError("Missing name")
       if  house not in ["Blue","Green","Red","Yellow"]:
           raise ValueError("Invalid house")
          
       self.name=name
       self.house=house
       self.marks=marks
       
    def __str__(self):  #__str__ method is a special method in Python that is called when you use the print function on an object
        return(f"{self.name} from {self.house} scored {self.marks} marks")
    
    def grade_check(self):
        match self.marks:
            case marks if marks<60:
                return "C grade"
            case marks if marks<80:
                return "B grade"
            case marks if marks>90 and marks<=100:
                return "A grade"
            case _:
                return "Invalid marks"

def get_student_info():
    name=input("Name: ")
    house=input("House: ")
    marks=input("Marks: ")
    try:
        student=Student(name,house,int(marks))  #constructor call to create a new Student object with the provided name and house
        return student
       
    except ValueError as e:
        print(e)
        

def main():     
    student=get_student_info()
    print(student) #passing object to print function will call the __str__ method of the Student class 
    print(student.grade_check()) #calling the grade_check method of the Student class to get the grade based on marks       

if __name__=="__main__":   #name is a special variable in Python that represents the name of the current module. When a Python file is run directly, its name is set to "__main__".    
    main()           
           