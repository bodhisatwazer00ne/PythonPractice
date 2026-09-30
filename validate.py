import re
#for regular expression
email=input("Enter your email: ").strip().lower()  #strip removes whitespace and lower converts to lowercase


# . any character except new line
# * 0 or more times
# + 1 or more times
# ? 0 or 1 time
# {m} m repeats
# {m,n} m to n repeats

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("Valid email")
else:
    print("Invalid email")
    
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S non-whitespace
# \w word character (alphanumeric or underscore)
# \W non-word character

    
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.+(edu|com|in|gov|org)$",email, re.IGNORECASE): #re.IGNORECASE makes the regex case-insensitive... it is a flag that can be passed as an argument to the re.search() function
        print("Valid email")
else:
    print("Invalid email")
    
    
    