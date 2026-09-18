#scope : local and global demo...

#Local scope
print("...Local scope...")
#A variable created inside a function can be accessed only within that function, this is called local scope
def function1():
    name = "John" #local variable
    print(name)

function1()
#print(name) #NameError: name 'name' is not defined

#Nested functions - accessing local variables
print("...Nested functions - accessing local variables...")
def function2():
    name = "Chris" #local variable
    def function3():
        print(name) #local variable is available for any function created inside that function
    function3()

function2()

#Global scope
print("...Global scope...")
#A variable that is created in the main Python body code and refers to the global scope;
# They can be accessed everywhere
age = 40 #gloabl variable
def function4():
    print(age)

function4()
print(age)

#We can have the same names for the local and global variables, but Python treats them differently
print("...We can have the same names for the local and global variables, but Python treats them differently...")
height = 6.2 #gloabl variable

def function5():
    height = 6.1 #local variable
    print(height)

function5()
print(height)

#Global keyword
print("...Global keyword...")
#Global variable can be created inside a function using 'Global' keyword
def function6():
    global weight # global variable created inside a function
    weight = 140

function6()
print(weight)

#Global keyword can be used to change the value of a global variable inside a function
print("...Global keyword can be used to change the value of a global variable inside a function...")
email = "learnPython.com"

def function7():
    global email
    email = "pythonEasyToLearn.com"

print(email)
function7()
print(email)