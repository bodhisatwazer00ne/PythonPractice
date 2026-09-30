class Student:
   def __init__(self,name,house):
       if not name:
           raise ValueError("Missing name")
       if  house not in ["Blue","Green","Red","Yellow"]:
           raise ValueError("Invalid house")
          
       self.name=name
       self.house=house
   
   
'''def get_student():
    student=Student()
    student.name=input("Enter student name: ")
    student.house=input("Enter student house: ")
    return student    '''                                                                      

def get_student_info():
    name=input("Name: ")
    house=input("House: ")
    try:
        student=Student(name,house)  #constructor call to create a new Student object with the provided name and house
        return student
    except ValueError as e:
        print(e)
        

def main():     
    student=get_student_info()
    print(f"{student.name} from {student.house}")
    
'''student=get_student()
    print(f"{student.name} from {student.house}")'''

    
    
if __name__=="__main__":     
    main()