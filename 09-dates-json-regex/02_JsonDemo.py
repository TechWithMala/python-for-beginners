#JSON demo

#import JSON module provided by Python
import json

#convert JSON to Python object(dictionary) using json.loads() function
print("...convert JSON to Python object(dictionary) using json.loads() function...")
sampleJson = '{"name":"Bob", "age":50, "height":5.7, "weight":175}'
pythonObj = json.loads(sampleJson)
print(pythonObj)
print(pythonObj["name"])
print(pythonObj["age"])
print(pythonObj["height"])
print(pythonObj["weight"])

#convert Python object(dictionary) to JSON using json.dumps() function
print("...convert Python object(dictionary) to JSON using json.dumps() function...")
pObj = {
    "name" : "Paul",
    "age" : 39,
    "height" : 5.9,
    "weight" : 179
}
json1 = json.dumps(pObj)
print(json1)

#convert Python object(tuple) to JSON using json.dumps() function
print("...convert Python object(tuple) to JSON using json.dumps() function...")
tuple1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(json.dumps(tuple1))

#convert Python object(list) to JSON using json.dumps() function
print("...convert Python object(list) to JSON using json.dumps() function...")
list1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(json.dumps(list1))

#convert Python object(string) to JSON using json.dumps() function
print("...convert Python object(string) to JSON using json.dumps() function...")
str2 = "Python is a programming language that lets you work more quickly and integrate your systems more effectively"
print(json.dumps(str2))

#convert int, float, boolean(true/false), none to JSON using json.dumps() function
print("..convert int, float, boolean(true/false), none to JSON using json.dumps() function..")
print(json.dumps(100))
print(json.dumps(100.4))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#example of a person object, convert to JSON using json.dumps() function
print("...example of a person object, convert to JSON using json.dumps() function...")
person = {
    "name" : "Shirley",
    "age" : 40,
    "height" : 5.8,
    "weight" : 137,
    "singleFamilyHome" : True,
    "townHome" : False,
    "kidsGirls" : ("Sam", "Pat"),
    "kidsBoys" : None,
    "trucks" : [
        {"model" : "Toyota Tundra", "engine" : "v8"},
        {"model" : "Toyota Tacoma", "engine" : "v6"}
    ]
}

print(json.dumps(person)) #not readable or user friendly format

#format json using 'indent'
print("...format json using 'indent'...")
print(json.dumps(person, indent=3)) #notice, and a space to separate each object; : and a space to separate keys and value

#replace default separator using 'separators'
print("...replace default separator using 'separators'...")
print(json.dumps(person, indent=3, separators=("; ", " ^")))

#order the result using 'sort_keys’
print("...order the result using 'sort_keys’...")
print(json.dumps(person, indent=3, separators=("; ", " ^"), sort_keys=True))