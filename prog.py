print("hello world")
print("Enter your name")
name=input()

first,last=name.split(" ")
print(f"First name= {first}")


#comment

"""multi line comments
sdfgjsgf
asdgasdg"""

'''multi line 
comments'''

age=input("Enter your age ")
print("Your age is "+age) #just concatanation
print("Your age is",age) #2 arguments for the print function....theay are sparated by a single space

print("hello",end="____")
print("Bodhisatwa")

print(f"Your age = {age}")


food=input("Your Favorite food ")
food=food.strip()  #remove whitespace from str

food=food.capitalize()#for first letter
print(food) 

food=food.title() #capitalize 1st letter each word
print(food)


school=input("Your School Name = ").strip().title()
print(school)






















