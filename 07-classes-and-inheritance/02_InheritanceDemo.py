#Inheritance demo...

#create a parent class, similar to how we create any other class
print("...create a parent class, similar to how we create any other class...")
class Person2:
    #use built-in __init__() function to assign values to attributes when the object is created
    def __init__(self, name, age, height, weight): #You can have any name, doesn't need to be self; self parameter is a reference to the current instance of a class
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def personFunction(self):
        print(self.name, self.age, self.height, self.weight)

person2 = Person2("Aly", 30, 5.6, 140) #init() will be called whenever an object is created
person2.personFunction()

#create a sub class by passing the parent class as a parameter
print("...create a sub class by passing the parent class as a parameter...")
class Person2Sub(Person2):
    pass #to create an empty class i.e. no statements within the class

#create a subclass that inherits the properties/functions from base class
print("...create a subclass that inherits the properties/functions from base class...")
class Person2Sub(Person2):
    person2Sub = Person2Sub("Sam", 35, 5.5, 120)
    person2Sub.personFunction() #Inheritance: accessing parent/base class function using subclass object reference

#use __init__() in subclass
#When we add __init__ in the subclass, it no longer inherits the properties/functions from the base class.
#To keep the inheritance of parent class, add a call to parent class __init__() function (or) use super() function
print("...use __init__() in subclass and add a call to parent class __init__() function...")
class Person2Sub(Person2):
    def __init__(self, name, age, height, weight):
        Person2.__init__(self, name, age, height, weight)

person2Sub = Person2Sub("Mike", 42, 5.6, 170)
person2Sub.personFunction()

print("...use __init__() in subclass and add a call to super() function...")
class Person2Sub(Person2):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

person2Sub = Person2Sub("Sean", 53, 5.9, 180)
person2Sub.personFunction()

#add properties to the subclass
print("...add properties to the subclass...")
class Person2Sub(Person2):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.email = "pythonEasyToLearn.com"

person2Sub = Person2Sub("Sean", 53, 5.9, 180)
print(person2Sub.email)

#refactor the above code by adding another parameter to subclass __init__ function
class Person2Sub(Person2):
    def __init__(self, name, age, height, weight, email):
        super().__init__(name, age, height, weight)
        self.email = email

person2Sub = Person2Sub("Sean", 53, 5.9, 180, "pythonEasyToLearn.com")
print(person2Sub.email)

#add functions to the subclass
print("...add functions to the subclass...")
class Person2Sub(Person2):
    def __init__(self, name, age, height, weight, email):
        super().__init__(name, age, height, weight)
        self.email = email

    def person2Function(self):
        print(self.name, self.age, self.height, self.weight, self.email)

person2Sub = Person2Sub("Chris", 44, 5.5, 190, "pythonEasyToLearn.com")
person2Sub.person2Function()