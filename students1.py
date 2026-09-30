import csv

students=[]

with open("students1.csv")as file:
    reader=csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        students.append({"name":row[0],"address":row[1]}) 
    #or after the reader is created, we can use the unpacking feature of python to get the name and address directly from the row
    #for name ,address in reader:
        #students.append({"name":name,"address":address})
  
for student in sorted(students , key=lambda student:student["address"]):
    print(f"{student['name']} is in {student['address']}")        
    
#for DictReader we need to mention the field name or row category in csv file 
    
with open("students1.csv")as file:
    reader=csv.DictReader(file)    
    for row in reader:
        students.append({"name":row["name"],"address":row["address"]})
        
        