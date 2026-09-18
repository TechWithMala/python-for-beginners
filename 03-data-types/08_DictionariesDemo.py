#Dictionaries demo...

#create a dictionary using curly brackets, written as key-value pairs
person = {
    "name": "Bob",
    "age": 40,
    "height": 6.1,
    "smokingStatus": False
}
print("...create a dictionary using curly brackets...")
print(person)

#create a dictionary using dict() constructor
person1 = dict(name="Craig", age=30, height=5.7, smokingStatus=True)
print("...create a dictionary using dict() constructor...")
print(person1)

#accessing dictionary element using key
print("...accessing dictionary element using key...")
print(person["name"])

#accessing dictionary element using get() function
print("accessing dictionary element using get() function")
print(person.get("age"))

#update the value of a dictionary element by referring key
print("...update the value of a dictionary element by referring key...")
print(person)
person["smokingStatus"] = True
print(person)

#loop through a dictionary to return keys
print("...loop through a dictionary to return keys...")
for personKeys in person:
    print(personKeys) #return keys

#loop through a dictionary to return values
print("...loop through a dictionary to return values...")
for personKeys in person:
    print(person[personKeys]) #return values

#loop through a dictionary to return values using values() function
print("...loop through a dictionary to return values using values() function...")
for personValues in person.values():
    print(personValues) #return values

#loop through a dictionary to return keys & values using items() function
print("...loop through a dictionary to return keys & values using items() function...")
for personKeys, personValues in person.items():
    print(personKeys, personValues)

#find the length of a dictionary using len() function
print("...find the length of a dictionary using len() function...")
print(len(person))

#check if the element exists in a dictionary using 'in' keyword
print("...check if the element exists in a dictionary using 'in' keyword...")
if "height" in person:
    print("element height exists in person dictionary...")

#add an element to a dictionary by using a new index and assign value to it
print("...add an element to a dictionary by using a new index and assign value to it...")
person["weight"] = 180
print(person)

#remove an element from a dictionary using pop() function
print("...remove an element from a dictionary using pop() function...")
person.pop("weight")
print(person)

#remove an element from a dictionary using popitem() function
print("...remove an element from a dictionary using popitem() function...")
person.popitem() #removes the last element
print(person)

#remove specified key using del keyword
print("...remove specified key using del keyword...")
del person["height"]
print(person)

#delete a dictionary completely using 'del' keyword
print("...delete a dictionary completely using 'del' keyword...")
#del person1
#print(person1) #NameError: name 'person1' is not defined

#empty a dictionary using clear() function
print("...empty a dictionary using clear() function...")
print(person1)
person1.clear()
print(person1)

#copy dictionary to another using copy() function
print("...copy dictionary to another using copy() function...")
anotherPerson = person.copy()
print(anotherPerson)

#copy dictionary to another using dict() function
print("...copy dictionary to another using dict() function...")
oneMorePerson = dict(person)
print(oneMorePerson)

#nested dictionaries : dictionary inside another
print("...nested dictionaries : dictionary inside another...")
person2 = {
    "father" : {
        "name" : "Craig",
        "age" : 50
    },

    "son" : {
        "name" : "Bryan",
        "age" : 15
    },

    "daughter" : {
        "name" : "Janet",
        "age" : 21
    }
}
print(person2)

#Or create three separate dictionaries
print("...Or create three separate dictionaries...")
father = {
        "name" : "Craig",
        "age" : 50
}

son = {
        "name" : "Bryan",
        "age" : 15
}

daughter = {
        "name" : "Janet",
        "age" : 21
}

person2 = {
    "father" : father,
    "son" : son,
    "daughter" : daughter
}

print(person2)