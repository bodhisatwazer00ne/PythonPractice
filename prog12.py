while True:
    try:
        x=int(input("Enter the number: "))
    except ValueError:  #A ValueError in Python happens when a function gets the right type of data, but an inappropriate value.
        print("x is not a number")     
    except Exception as e:
        pass   
    else:
        break

print(f"x is {x}")    

#pass statement -it does nothing, but it lets your code run without errors             
#raise statement - it raises an exception, you can specify the type of exception and the message to be displayed when the exception is raised             
'''
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
'''
