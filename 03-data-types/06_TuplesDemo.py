#Tuples Demo...

#create tuples using round brackets
tuple1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("...create tuples using round brackets...")
print(tuple1)

#create a tuple using tuple() constructor
tuple11 = tuple(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
print("...create a tuple using tuple() constructor...")
print(tuple11)

#create a tuple with only one element using comma
tuple2 = ("Craig",)
print("...create a tuple with only one element using comma...")
print(tuple2)

#accessing tuple elements using index number
print("...accessing tuple elements using index number...")
print(tuple1[2])

#return the tuple elements from the end using the negative index number
print("...return the tuple elements from the end using the negative index number...")
print(tuple1[-1]) #-1 refers to the last element in the tuple

#return the range of elements using index
print("...return the range of elements using index...")
print(tuple1[1:3]) #index 3 is excluded
print(tuple1[:4]) #index 4 is excluded
print(tuple1[1:])

#return the range of elements from the end using the negative index number
print("...return the range of elements from the end using the negative index number...")
print(tuple1[-3:-1]) # -3 included, -1 is excluded

#update the existing elements in tuple - tuples are unchangeable i.e. immutable
#convert tuple to list, update the list and convert back to tuple
print("...update the existing elements in tuple...")
list1 = list(tuple1)
list1[1] = "Sunday"
tuple1 = tuple(list1)
print(tuple1)

#loop through a Tuple
print("...loop through a Tuple...")
for temp in tuple1:
    print(temp)

#check if the element exists in a tuple
print("...check if the element exists in a tuple...")
if "Sunday" in tuple1:
    print("Element Sunday exists in tuple1")

#find the length of a tuple using len() function
print("...find the length of a tuple using len() function...")
print(len(tuple1))

#add an element to a tuple – unchangeable
print("...add an element to a tuple – unchangeable...")
#tuple1[1] = "Saturday" #TypeError: 'tuple' object does not support item assignment
#print(tuple1)

#remove an element from a tuple
#tuples are unchangeable, so we cannot remove an element from a tuple, but can delete the tuple completely
print("...remove an element from a tuple...")
#del tuple1
#print(tuple1) #NameError: name 'tuple1' is not defined

#concatenate two tuples using + operator
print("...concatenate two tuples using + operator...")
tuple2 = ("apple", "orange")
tuple3 = ("banana", "grapes")
print(tuple2 + tuple3)