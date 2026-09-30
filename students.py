with open("students.csv", "r") as file:
    for line in file:
        row=line.strip().split(",")
        print(f"{row[0]} is in {row[1]} House ")
        
with open("students.csv" ) as file:
    for line in file:
        name,house=line.strip().split(",")
        print(f"{name} is in {house} House")       
        
students=[]        
with open("students.csv" ) as file:
    for line in file:
        name,house=line.strip().split(",")
        students.append(f"{name} is in {house}")
        
for student in students:        
    print(student)       
    
            
students=[]  
#dictionary    
with open("students.csv" ) as file:
    for line in file:
        name,house=line.strip().split(",")
        studdict={}
        studdict["name"]=name    
        studdict["house"]=house
        students.append(studdict)
        
for student in students:        
    print(f"{student['name']} is in {student['house']}")
    
def get_name(student):
    return student["name"]

students.sort(key=get_name)  #sort by name

print("After sorting by name")

for student in students:
    print(f"{student['name']} is in {student['house']}")
    
    
for student in sorted (students, key =get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
    
for student in sorted (students, key =lambda student: student["house"]):        #alambda function is an anonymous function that can take any number of arguments, but can only have one expression...since we are using this func only once
    print(f"{student['name']} is in {student['house']}")    