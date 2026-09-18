#Iterators demo...

#iterate strings using iter(), next()
print("...iterate strings using iter(), next()...")
str = "python"
strIter = iter(str) #returns an iterator using iter() function
print("Iterate string object...")
print(next(strIter)) #return each value inside an iterator object
print(next(strIter))
print(next(strIter))
print(next(strIter))
print(next(strIter))
print(next(strIter))

#use for loop to iterate an iterable object - string
print("...use for loop to iterate an iterable object - string...")
for str1 in str:
    print(str1)

#iterate tuple object using iter(), next()
print("...iterate tuple object using iter(), next()...")
tuple1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
tupleIter = iter(tuple1) #returns an iterator using iter() function
print("Iterate tuple object...")
print(next(tupleIter)) #return each value inside an iterator object
print(next(tupleIter))
print(next(tupleIter))
print(next(tupleIter))
print(next(tupleIter))

#use for loop to iterate an iterable object – tuple
print("...use for loop to iterate an iterable object – tuple...")
for tuples in tuple1:
    print(tuples)

#similary, we can iterate other iterable objects(lists, dictionaries, sets, etc,..)