#Conditionals <,>,<=,>=,==,!=
#if statement


if 5>3:
    print("5 is greater than 3")
    
#elif statement
age=int(input("Enter your age "))
if age==18:        
    print("You are 18")
elif age>18:
    print("You are above 18")
elif age<18:    
    print("You are below 18")
    
    
#else statement
n=int(input("Enter a number "))    
if n%2==0:
    print("Even")
else :
    print("Odd")    

#or     
x=20
y=10

if x>y or y>x:
    print("x and y are not equal")
else:
    print("x and y are equal")    
    
if x==y:
    print("x and y are equal")    
else :
    print("x and y are not equal")    
    
    
#and
score=int(input("Enter your score ")) 
if score>=90 and score<=100:
    print("A grade")   
elif 80 <= score < 90:          #python allows this 
    print("B grade")    
else:
    print("C grade")    