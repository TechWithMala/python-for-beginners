#Sets demo...

#create a set using curly brackets
set1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print("...create a set using curly brackets...")
print(set1)

#create a set using set() constructor
set11 = set(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
print("create a set using set() constructor")
print(set11)

#access set elements using for loop
#sets are unordered, so the elements have no index; Hence we cannot use index to access set elements
print("...access set elements using for loop...")
for setElement in set1:
    print(setElement)

#check if a specific element exists in a set using 'in' keyword
print("...check if a specific element exists in a set using 'in' keyword...")
print("Thursday" in set1)

#find the length of a set using len() function
print("...find the length of a set using len() function...")
print(len(set1))

#add an element to a set using add() function
print("...add an element to a set using add() function...")
set1.add("Sunday")
print(set1)

#add more than one element using update() function
print("...add more than one element using update() function...")
set1.update(["Saturday", "Monday1"])
print(set1)

#remove an element from a set using remove() function
print("...remove an element from a set using remove() function...")
set1.remove("Monday1")
print(set1)
#set1.remove("Monday1") #KeyError: 'Monday1'
#print(set1)

#remove an element from a set using discard() function
print("...remove an element from a set using discard() function...")
set1.discard("Saturday")
print(set1)
set1.discard("Saturday") #doesn't throw any error like remove()
print(set1)

#remove an element using pop() function
print("...remove an element using pop() function...")
removedElement = set1.pop() #removes the last element from a set
print(removedElement) #unordered, so we will not know which element gets removed
print(set1)

#Empty a set using clear() function
print("...Empty a set using clear() function...")
print(set11)
set11.clear()
print(set11)

#Delete a set completely using ‘del’ keyword
print("...Delete a set completely using ‘del’ keyword...")
#del set11
#print(set11) #NameError: name 'set11' is not defined

#Concatenate two sets using union()
setXyz = {"x", "y", "z"}
setAbc = {"A", "B", "C"}

setXyzAbc = setXyz.union(setAbc)
print("...Concatenate two sets using union()...")
print(setXyzAbc)

#Concatenate two sets using update()
print("...Concatenate two sets using update()...")
setXyz.update(setAbc)
print(setXyz)
