#Operators demo...

#We can perform operations on variables using operators

#1. Arithmetic operators : to perform mathematical operations...
print("Arithmetic operators...")
num1 = 9
num2 = 3
print("addition operator...")
print(num1+num2)

print("subtraction operator...")
print(num1-num2)

print("multiplication operator...")
print(num1*num2)

print("division operator...")
print(num1/num2)

print("modulus operator...")
print(num1%num2)

print("exponentiation operator...")
print(num1 ** num2) #9*9*9

print("floor division operator...")
print(num1 // num2)
print(9 // 2) #rounds the result to the nearest whole number

#2. Assignment operators : to assign values
print("Assignment operators...")
num3 = 3
print(num3)

print("addition operator...")
num3 += 2 #num3 = num3+2
print(num3)

print("subtraction operator...")
num3 -= 2 #num3 = num3-2
print(num3)

print("multiplication operator...")
num3 *= 2 #num3 = num3*2
print(num3)

print("division operator...")
num3 /= 2 #num3 = num3/2
print(num3)

print("modulus operator...")
num3 %= 2 #num3 = num3%2
print(num3)

print("floor division operator...")
num3 = 5
num3 //=2 #num3 = num3 // 2
print(num3)

print("exponentiation operator...")
num3 = 2
num3 **= 2 #num3 = num3 ** 2
print(num3)

#3. Comparison operators : to compare two values
print("Comparision operators...")
num1 = 4
num2 = 2

print("Equal operator...")
print(num1 == num2)

print("Not Equal operator...")
print(num1 != num2)

print("Greater than operator...")
print(num1 > num2)

print("Greater than or Equal to operator...")
print(num1 >= num2)

print("Less than operator...")
print(num1 < num2)

print("Less than or Equal to operator...")
print(num1 <= num2)

#4. Logical operators : to combine conditional statements
num = 4
print("Logical operators...")
print("and operator...")
print(num==4 and num>2) #returns true if both the statements are true

print("or operator...")
print(num==4 or num>2) #returns true if one of the statements are true

print("not operator...")
print(not(num == 4)) #reverses the result

#5. Identity operators : to compare the objects(same memory location or not)
print("Identity operators...")
list1 = ["John", "Chris"]
list2 = ["John", "Chris"]
list3 = list2

print("is operator...")
print(list1 is list2) #objects list1 and list2 with different memory locations
print(list2 is list3) #list2 and list3 are same objects memory locations
print(list1 == list2) #comapres the content

print("is not operator...")
print(list1 is not list2) #objects list1 and list2 with different memory locations
print(list2 is not list3) #list2 and list3 are same objects memory locations
print(list1 != list2) #comapres the content

print("#6. Membership operators : to test if the value exists in the object")
print("Membership operators...")
list1 = ["Python", "Java"]

print("in operator...")
print("Python" in list1)

print("not in operator...")
print("Python" not in list1)

#7. Bitwise operators : to compare binary numbers, operates bit by bit
print("Bitwise operators...")
num1 = 10 #0000 1010
num2 = 4 #0000 0100

print("Bitwise AND operator...")
print(num1 & num2) #0 sets each bit to 1 if both bits are 1

print("Bitwise OR operator...")
print(num1 | num2) #14 = 0000 1110 sets each bit to 1 if one of the bits is 1

print("Bitwise XOR operator...")
print(num1 ^ num2) #14 = 0000 1110 sets each bit to 1 if only one of the two bits is 1

