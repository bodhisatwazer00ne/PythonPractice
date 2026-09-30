def main():
    x=int(input("Enter the number "))
    if is_even(x):
        print(x," is even")
    else:
        print(x," is odd")    
        
def is_even(n):
    return True if n%2==0 else False        #python allows this instead of if else statement
#we can replace it with
#return n%2==0  #this will return true or false directly without using if else statement

main()