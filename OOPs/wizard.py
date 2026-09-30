class Wizard:
    def __init__(self,name,house):
       if not name:
           raise ValueError("Missing name")
       self.name=name
       if house not in ["Blue","Green","Red","Yellow"]:
           raise ValueError("Invalid house")            
       self.house=house

class Student(Wizard):
    def __init__(self,name,house):  #super() is a built-in function in Python that returns a temporary object of the superclass (parent class) that allows you to call its methods
        super().__init__(name,house)
        self.name=name
        self.house=house
        
        

class Professor(Wizard):
    def __init__(self,name,house):
        super().__init__(name,house)
        self.name=name
        self.house=house        
        
student=Student("Harry Potter","Blue")
print(f"{student.name} from {student.house}")
professor=Professor("Severus Snape","Green")  
print(f"{professor.name} from {professor.house}")      
        
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a subclass or derived class) to inherit attributes and methods from another class 
        