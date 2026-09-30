def main():
    hello("Bodhisatwa")
    goodbye("Bodhisatwa")

def hello(name):
    print(f"Hello {name}")
    
    
def goodbye(name):
    print(f"Goodbye {name}")    

if __name__ == "__main__":  #this code will only run if this file is executed directly, not when imported as a module    
    main()   