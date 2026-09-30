class Student:
    def __init__(self,name,house):
                
        self.name=name
        self.house=house #calls the setter method for house attribute
   
    def __str__(self):  #__str__ method is a special method in Python that is called when you use the print function on an object
        return(f"{self.name} from {self.house}")
    
#property is used to define a getter method for the house attribute. It allows you to access the house attribute using dot notation (e.g., student.house) instead of calling method with parentheses 
        
#@property is a Python decorator that lets you treat a method like an attribute.
#property is a built-in Python decorator that converts a method into a property (attribute), allowing the method to be accessed using normal attribute syntax without parentheses.

    @property
    def house(self): #getter method 
        return self._house 
    
    @house.setter
    def house(self,house):#setter method 
        if  house not in ["Blue","Green","Red","Yellow"]:
           raise ValueError("Invalid house")
        self._house=house                                                                  

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
           raise ValueError("Missing name")
        self._name=name
        
def get_student_info():
    name=input("Name: ")
    house=input("House: ")
    return Student(name,house)  
  
        

def main():     
    student=get_student_info()
    print(student)
 
    
    
if __name__=="__main__":     
    main()