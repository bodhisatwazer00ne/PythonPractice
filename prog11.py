#list - data structure to store multiple values in a single variable
#list can store different types of data    
#mylist=[1,2,3,"hello",4.5]

fruits = ["apple", "banana", "cherry"]
print(fruits)  
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)

fruits.append("mango")     # Add at end
fruits.insert(1, "grape")  # Add at specific index


fruits.remove("apple")  # Remove by value
fruits.pop()            # Remove last item
del fruits[0]           # Remove by index


#looping through the list
for fruit in fruits:
    print(fruit)


numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # [2, 3, 4]
print(numbers[:3])   # [1, 2, 3]
print(numbers[::-1]) # Reverse list


nums = [3, 1, 4, 1, 5]

nums.sort()     # Sort list
nums.reverse()  # Reverse list
print(len(nums))  # Length
print(max(nums))  # Maximum value
print(min(nums))  # Minimum value

#A compact way to create lists:
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


#Nested Lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3


#dictionary dict key value pairs
'''
student = {"name": "Alice", "age": 20, "grade": 85}
print(student["name"])  # Alice
print(student.get("age"))  # 20
student["age"] = 21  # Update value
student["city"] = "New York"  # Add new key-value pair
del student["grade"]  # Remove key-value pair
print(student)  # {'name': 'Alice', 'age': 21, 'city': 'New York'}
'''

students={
    "Hermione":"Gryffindor",
    "Draco":"Slytherin",
    "Snape":"Slytherin",
}

for student in students:
    print(student,students[student])
    
    
children=[
    {"name":"Alice","age":10,"grade":5},
    {"name":"Bob","age":12,"grade":6},
    {"name":"Charlie","age":11,"grade":7},
    {"name":"David","age":13,"grade":None}
]    

for child in children:
    print(child["name"])
    print(child["name"], child["age"],child["grade"], sep=",")