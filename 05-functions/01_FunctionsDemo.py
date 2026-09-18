#Functions demo...

#Create a function using 'def'
def function1():
    print("I'm in function1()...")

#Call a function
function1()

#Pass parameters or arguments
print("...Pass parameters or arguments...")
def function2(name): #parameter
    print("I'm in function2()...")
    print("name is: " + name)

function2("Bob") #argument

#pass multiple parameters - comma separated
def function3(name, age, height, smokingStatus):
    print("{} is {} years old, height is {} and smoking status is {}".format(name, age, height, smokingStatus))

function3('Bob', 40, 6.5, False)
#should call the function with the correct number of arguments - 4
#function3(40, 6.5, False) #TypeError: function3() missing 1 required positional argument: 'smokingStatus'

#Keyword arguments : send arguments as key-value pair, so order of the arguments doesn't matter
def function4(lastName, firstName, middleName):
    print("last name is : " + lastName)

function4(firstName="Bob", middleName="K", lastName="XYZ")

#Arbitrary arguments : add * before the parameter name if we don't know how many number of arguments will be passed
def function5(*names):
    print("First name is : " + names[0])

function5("Bob", "M", "Xyz")

#Arbitrary keyword arguments : add ** before the parameter when we don't know how many keyword arguments will be passed
def function6(**names):
    print("Middle name is : " + names["middleName"])

function6(firstName="Bob", middleName="H", lastName="Xyz")

#Default parameters
def function7(state="Colorado"):
    print("I live in " + state)

function7("California")
function7("Texas")
function7()
function7("Arizona")
function7("Idaho")

#passing different datatypes as arguments
def function8(list):
    print("Days in a week...")
    for temp in list:
        print(temp)

function8(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

#return values using the return keyword
def returnFunction(value):
    return value/7

print(returnFunction(70))

#pass statement and usage
def emptyDefFunction():
    pass

#function can return boolean values (true/false)
def boolFunction(name):
    if name == "Bob":
        return True
    else :
        return False

print(boolFunction("Bob"))
print(boolFunction("Chris"))