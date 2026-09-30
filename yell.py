def main():
    yell("WASSUP!","dawg","COOOL")
    
def yell(*words): # *words args for multiple positional arguments
    uppercased=[word.upper() for word in words]
    print(*uppercased)
    
    uppercased=map(str.upper,words) #functional programming    
    print(*uppercased)
    
if __name__ =="__main__":
    main()        