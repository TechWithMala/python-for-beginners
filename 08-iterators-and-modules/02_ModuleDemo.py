#using module functions or variables demo...

#use the module using the 'import' keyword
import Helper
#use the functions from the module as module name.function name
print("...use the functions from the module as module name.function name...")
Helper.add(10, 5)
Helper.sub(10, 5)
Helper.mul(10, 5)
Helper.div(10, 5)

#use the variables from the module as module name.variable name
print("...use the variables from the module as module name.variable name...")
name = Helper.person["name"]
print(name)
print(Helper.person["age"])
print(Helper.person["height"])
print(Helper.person["weight"])

#import only specific function of a module using 'from' keyword
print("...import only specific function of a module using 'from' keyword...")
from Helper import mul
mul(20, 10) #don't use the module name, access the function directly

#rename a module by creating an alias using 'as' keyword
print("...rename a module by creating an alias using 'as' keyword...")
import Helper as help
print(help.person["age"])

#import the built-in modules provided by Python
print("...import the built-in modules provided by Python...")
import platform
print(platform.system())

#use dir function to list all the functions and variables available in a module
print(dir(Helper))