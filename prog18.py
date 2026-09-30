name=input ("Your name ")

file=open("names.txt", "w")
file.write(name)
file.close()
#this program will take your name as input and write it to a file called names.txt. 
# The file is opened in write mode, which means that if the file already exists, its contents will be overwritten. 
# After writing the name to the file, the file is closed to ensure that all data is properly saved and resources are released.


surname=input("Your Surname ")
file=open("surnames.txt", "a")
file.write(f"{surname}\n")
file.close()
#a is used to append to the file instead of overwriting it.dg This way, if the file already exists, the new surname will be added to the end of the file rather than replacing its contents.

with open("surnames.txt", "r") as file:
    surname=file.readlines()
    print(f"Your surname is {surname}")
#with statement is used to automatically take care of closing the file 

with open("surnames.txt", "r") as file:
    lines=file.readlines()
     
for line in lines:
    print("Hello,", line.rstrip())     
#rstrip is used to remove any trailing whitespace characters (including the newline character) from the end of each line before printing it.      

with open("surnames.txt", "r") as file:
    for line in file:
        print("All the best ", line.rstrip())
#rstrip vs strip is that rstrip removes whitespace only from the right side of the string, while strip removes whitespace from both sides of the string.         
        
surnames = []      #make a list to store the surnames

with open("surnames.txt", "r") as file:        
    for line in file:
        surnames.append(line.strip()) #add the surname to the list from the file, removing any leading/trailing whitespace
        
for surname in sorted(surnames):  #sort the surnames in alphabetical order and print them
    print(f"Hello, {surname}")        

for surname in sorted(surnames, reverse=True):  #sort the surnames in reverse alphabetical order and print them
    print(f"Hello, {surname}")      
    
with open("surnames.txt", "r") as file:
    for line in sorted (file):  #sort the surnames in the file itself in alphabetical order and print them
        print(f"Lesgooo, {line.strip()}")     
    