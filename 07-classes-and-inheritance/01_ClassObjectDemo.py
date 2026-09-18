#Class and object demo...

#creating a class using 'class' keyword
print("...creating a class using 'class' keyword...")
class Person:
    age = 40 #class attribute

person = Person() #create an object to Person class
print(person.age) #access Person class attribute, age

#use built-in __init__() function to assign values to attributes when the object is created
print("...use built-in __init__() function to assign values to attributes when the object is created...")
class Person1:
    def __init__(self, name, age, height, weight): #self parameter is a reference to the current instance of the class
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

person1 = Person1("Aly", 30, 5.6, 130) #init() will be called
print(person1.name)
print(person1.age)
print(person1.height)
print(person1.weight)

#class user defined methods
print("...class user defined methods...")
class Person2:
    def __init__(self, name, age, height, weight): #self parameter is a reference to the current instance of the class
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def personFunction(self):
        print(self.name, self.age, self.height, self.weight)

person2 = Person2("Aly", 30, 5.6, 130) #init() will be called
person2.personFunction()

#set values to the attributes
print("...set values to the attributes...")
print(person2.name)
person2.personFunction()
person2.name = "Jeff"
print(person2.name)
person2.personFunction()

#delete attribute values using 'del' keyword
print("...delete attribute values using 'del' keyword...")
print(person2.age)
del person2.age
#print(person2.age) #AttributeError: 'Person2' object has no attribute 'age'

#delete objects using 'del' keyword
del person2
#print(person2.name) #NameError: name 'person2' is not defined

#use 'pass' statement to write empty class
class Person3:
    pass