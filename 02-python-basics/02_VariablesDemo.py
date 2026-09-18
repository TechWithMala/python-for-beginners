#Variables demo...

#Variables are created as soon as you assign value to it
name = "Bob" #string variable
print(name)

#Variables doesn’t need to be created with any specific datatype; they can be changed after they are set
test = 7 #int variable
test = 'seven' #string variable
print(test)

#String variables can be created either by using single or double quotes
name1 = "Bob"
name2 = 'Bob'
print(name1)
print(name2)

#We can assign different value to multiple variables in one line
name1, name2, name3 = "Bob", "Craig", "John"
print(name1)
print(name2)
print(name3)

#We can assign same value to multiple variables in one line
name1 = name2 = name3 = "Bob"
print(name1)
print(name2)
print(name3)

#Concatenation operator: +
name = "John"
age = 40
height = 6
print("My name is: " + name)
#print(name + age) #TypeError: can only concatenate str (not "int") to str
print(age + height) #Arithmetic operator