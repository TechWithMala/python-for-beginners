#Exception handling demo...

#try and except blocks
print("...try and except blocks...")
try:
    print(2/0) #ZeroDivisionError: division by zero
except:
    print("An exception occurred in the try block...")

try:
    print("test value is : " + test) #NameError: name 'test' is not defined
except:
    print("Please define test variable...")

try:
    age = int(input("Enter age :")) #ValueError: invalid literal for int() with base 10:
    print(age)
except:
    print("Please enter age value in numbers only...")

#more than one except block
print("...more than one except block...")
try:
    print(2/0) #ZeroDivisionError: division by zero
except ZeroDivisionError: #most specific
    print("ZeroDivisionError occurred...")
except: #most generic
    print("An exception occurred in the try block...")

#use 'else' keyword to execute a block of code when there are NO exceptions raised
print("...else keyword...")
try:
    print("Exception handling...")
except:
    print("An exception occurred...")
else:
    print("easy to learn...")

#finally block
print("...finally block...")
try:
    print(2/0) #ZeroDivisionError: division by zero
except ZeroDivisionError: #most specific
    print("ZeroDivisionError occurred...")
finally:
    print("finally block gets executed regardless of exception raised/caught or not...")

#use 'raise' keyword to throw/raise an user friendly exception
height = 6
if not type(height) is float:
    raise TypeError("height needs to be floating point number...") #TypeError: height needs to be floating point number...