#Strings demo...

#multiple lines can be assigned to a variable using three single or double quotes
str1 = 'python'
str2 = '''Python is a programming language that lets you work more quickly 
        and integrate your systems more effectively.'''
str3 = """Python is a programming language that lets you work more quickly 
        and integrate your systems more effectively."""

print("....string values....")
print(str1)
print(str2)
print(str3)

#access elements of a string
print(".....access elements of a string.....")
print(str1[2])
print(str2[15])

#length of a string
print(".....length of a string.....")
print(len(str1))

#slicing - to return a range of characters by specifying start and end index
print(".....slicing.....")
print(str1[1:3]) #character at the position 3 is excluded

#Negative index - to return a range of characters from the end of a string
strN = 'python'
print(".....Negative index.....")
print(strN[-3:-1])

#Use strip() to remove white spaces
str4 = " python "
print("....strip().....")
print(str4.strip())

#Use lower() to return a string in lower case
str5 = "PYTHON"
print(".....lower().....")
print(str5.lower())

#use upper() to return a string in upper case
print(".....upper().....")
print(str1.upper())

#use 'in', 'not in' to check if a phrase present or not
str6 = "python programming language"
print(".....in', 'not in'.....")
print("prog" in str6)
print("prog" not in str6)

#use replace() to replace a string
print("....replace()....")
print(str1.replace("h", "x"))

#use split() to split a string
print("....split()....")
print(str2.split())

#concatenate strings using + operator
str7 = "python"
str8 = "programming"
print(".....concatenate strings....")
print(str7 + " " + str8) #" " to add space between strings

#combining strings with other datatypes using format()
name = "Bob"
age = 40
height = 6.5
smokingStatus = False
print(".....format().....")
#print(name + "is" + age + "years old") ##combining strings with other datatypes using format()
print("{} is {} years old, height is {} and smoking status is {}".format(name, age, height, smokingStatus))

#use escape characters to insert characters that are illegal in a string
print("....escape characters....")
print("python is a \"scripting\" language.....")