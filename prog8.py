#match

name=input("Enter your name ")


match name:
    case "Harry":
        print("Gryffindor!")
    case "Ron":
        print("Gryffindor!")
    case "Hermione":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case "Snape" | "Voldemort" | "Bellatrix":  #or operator for multiple cases
        print("Slytherin!")
    case "Dumbledore":
        print("Gryffindor!")
    case _:  #for cases which are not handled above
        print("Hello, stranger!")