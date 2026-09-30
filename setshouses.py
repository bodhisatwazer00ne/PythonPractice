students=[
    {"name":"Hermoine","House":"Gryffindor"},
    {"name":"Harry","House":"Gryffindor"},
    {"name":"Draco","House":"Slytherin"},
    {"name":"Pamrea","House":"Ravenclaw"},
]

houses=set()

for student in students:
    houses.add(student["House"])
    
for house in sorted(houses,reverse=True):
    print(house)    
    
    
    
total=50

def housestotal():
    global total
    total+=10

def studtotal():
    global total
    total-=20        
    
def main():    
    print(total)
    housestotal()
    print(total)
    studtotal()
    print(total)
    
main()    