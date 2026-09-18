#Regular expression demo...

#import regular expression module
import re

#RegEx functions: search() function : searches a string with the RegEx specified
print("...search()....")
inputStr = "welcome to python programming language"
searchResult = re.search("^wel*.*age$", inputStr) #^ - starts with; $ - ends with; * - zero or more occurrences
print(searchResult) #returns the match object
if(searchResult):
    print("string starts with 'wel' and ends with 'age'...")
else:
    print("No match found....")

print(re.search("hello", inputStr)) #returns None when there is no match

#RegEx functions: findall() function : returns a Python list that contains all the matches
print("...findall()...")
inputStr = "My contact number is 8012345678 and my spouse number is 8018765432"
findallResult = re.findall("\d+", inputStr) #RegEx to find all digits in a string inputStr
print(findallResult)

#RegEx functions: split() function : returns a Python list of strings after splitting the string by the specified match
inputStr = "welcome to python programming language"
splitResult = re.split("\s", inputStr) #split the string inputStr at each white space
splitResult1 = re.split("\s", inputStr, 2) #split the string only in two occurrences of space
print(splitResult)
print(splitResult1)

#RegEx functions: sub() function : replaces a string that matches the RegEx instead of the perfect match of a string
inputStr = "welcome to python programming language"
subResult = re.sub("\s", ".", inputStr)
subResult1 = re.sub("\s", ".", inputStr, 1) #replace space with a . only at first occurrence
print(subResult)
print(subResult1)