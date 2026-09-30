def main():
    name=input("What's your name? ")    
    hello(name)   #parameter 
    

def  hello(to="world"):          #to argument   = and world for default if no params passed
    print("Hello",to )
    
main()
hello()
hello("WEsr")
    