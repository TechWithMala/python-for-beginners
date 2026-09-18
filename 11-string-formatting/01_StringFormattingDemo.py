#String formatting demo...

#use {} as a placeholder
name = input("Enter name: ")
strInput = "My name is {}"
print(strInput.format(name)) #{} will be replaced by name

#multiple values can be used by adding more placeholders in format() function
print("...multiple values can be used by adding more placeholders in format() function...")
name = "Joe"
age = 45
height = 5.9
married = True
housePrice = 500000

person = "{} is {} years old, height is {} and marital status is {}"
print(person.format(name, age, height, married))

#use the index numbers
print("...use the index numbers...")
person1 = "{0} is {1} years old, height is {2} and marital status is {3}"
print(person1.format(name, age, height, married))

#format the value with specific data type
print("...format the value with specific data type...")
houseValue = "The home value is {:.2f} dollars"
print(houseValue.format(housePrice))

#named indexes can be used by placing a name inside a curly bracket
# and the same name has to be used when passing parameter values
print("...named indexes...")
person = "{name} is {age} years old, height is {height} and marital status is {married}"
print(person.format(name = "Jim", age = 50, height = 5.6, married = False))