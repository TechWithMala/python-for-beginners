#Arrays demo...

#creating an array using square brackets
print("...creating an array using square brackets...")
array1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(array1)

#accessing array elements using index number
print("...accessing array elements using index number...")
print(array1[3]) #index starts from 0

#update the existing element in the array
print("...update the existing element in the array...")
array1[1] = "Sunday"
print(array1)

#find the length of an array using len() function
print("...find the length of an array using len() function...")
print(len(array1))

#loop through an array using for loop
print("...loop through an array using for loop...")
for temp in array1:
    print(temp)

#add an element to the end of an array using append() function
print("...add an element to the end of an array using append() function...")
array1.append("Saturday")
print(array1)

#remove an element from an array using remove() function
print("...remove an element from an array using remove() function...")
array1.remove("Saturday")
print(array1)

#remove() function removes only first occurrence of an element of an array
print("...remove() function removes only first occurrence of an element of an array...")
array2 = ["apple", "orange", "grapes", "apple"]
array2.remove("apple")
print(array2)

#remove an element of an array at the specified index using pop() function
print("...remove an element of an array at the specified index using pop() function...")
array1.pop(2)
print(array1)
array1.pop()
print(array1) #it removes the last element from the array if index is not specified

