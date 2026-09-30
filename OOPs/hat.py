import random

class Hat:
    houses=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls,name):  
        print(name, "is in", random.choice(cls.houses)) 
#@classmethod is a built-in Python decorator that makes a method belong to the class rather than a particular object/instance.
        
Hat.sort("Harry Potter")        