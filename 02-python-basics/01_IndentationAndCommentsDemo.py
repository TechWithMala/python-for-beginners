#Indentation and comments demo...

a = 4
b = 2

if a > b:
    print("a is greater than b...")

#IndentationError - we skipped space at the beginning of the line near print function
#multi-line comments : insert # for each line
#if a > b:
#print("a is greater than b...")

#multi-line comments : multi-line string
"""
if a > b:
print("a is greater than b...")
"""

#we can give any number of spaces within the different blocks
if a > b:
    print("a is greater than b...")
if a > b:
        print("a is greater than b...")

#IndentationError - has to use the same number of spaces within the same block
if a > b:
    print("a is greater than b...")
        print("a is greater than b...")