#Lists demo...

#create a list using square brackets
print("...create a list using square brackets...")
list1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(list1)

#create a list using list() constructor
print("...create a list using list() constructor...")
list1 = list(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
print(list1)

#access list elements using index number
print("...access list elements using index number...")
print(list1[3])

#return the list elements from the end using the negative index number
print("...return the list elements from the end using the negative index number...")
print(list1[-2]) #-1 refers to the last element in the list
print(list1[-1])

#return the range of elements using index
print("...return the range of elements using index...")
print(list1[1:3]) #index 3 is excluded
print(list1[:4]) #index 4 is excluded
print(list1[1:])

#return the range of elements from the end using the negative index number
print("...return the range of elements from the end using the negative index number...")
print(list1[-3:-1]) #-3 included, -1 excluded

#update the existing element in the list
print("...update the existing element in the list...")
list1[1] = "Sunday"
print(list1)

#loop through a list
print("...loop through a list...")
for temp in list1:
    print(temp)

#check if the element exists
print("...check if the element exists...")
if "Sunday" in list1:
    print("Element Sunday exists in list1")

#find the length of a list using len() function
print("...len() function...")
print(len(list1))

#add an element to the end of a list using append() function
print("...add an element to the end of a list using append() function...")
list1.append("Saturday")
print(list1)

#add an element at the specified index using insert() function
print("...add an element at the specified index using insert() function...")
list1.insert(1, "Tuesday")
print(list1)

#remove an element from a list using remove() function
print("...remove an element from a list using remove() function...")
list1.remove("Sunday")
print(list1)

#remove an element at the specified index using pop() function
list1.pop(2)
list1.pop() #it removes last element from the list if index is not specified
print(list1)

#remove specified index using del keyword
print("...remove specified index using del keyword...")
del list1[2] #if we do not specify the index, it removed the list completely
print(list1)

#empty a list using clear() function
print("...empty a list using clear() function...")
list1.clear()
print(list1)

#copy from one list to another list using copy() function
list2 = ["Bob", "Craig", "Chris"]
list3 = list2.copy()
print("...copy from one list to another list using copy() function...")
print(list2)
print(list3)

#copy from one list to another list using list() function
print("...copy from one list to another list using list() function...")
list4 = list(list3)
print(list4)

#concatenate two lists using + operator
list5 = list3 + list4
print("...concatenate two lists using + operator...")
print(list5)

#concatenate two lists using append operator
print("...concatenate two lists using append operator...")
for element in list3:
    list4.append(element)
print(list4)

#concatenate two lists using extend() function
list3.extend(list4)
print("...concatenate two lists using extend() function...")
print(list3)
