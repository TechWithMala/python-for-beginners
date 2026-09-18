#Python numeric data types demo - int, float and complex numbers

#int
intNum1 = 77
intNum2 = -777
intNum3 = 7777777777

print(".....integers demo.....")
print(intNum1)
print(type(intNum1))
print(intNum2)
print(type(intNum2))
print(intNum3)
print(type(intNum3))

#float
floatNum1 = 3.3
floatNum2 = 3.30
floatNum3 = -3.33
floatNum4 = -3.3e10 #scientific numbers with an "e" to indicate the power of 10.

print(".....floating point numbers.....")
print(floatNum1)
print(type(floatNum1))
print(floatNum2)
print(type(floatNum2))
print(floatNum3)
print(type(floatNum3))
print(floatNum4)
print(type(floatNum4))

#complex
complexNum1 = 9+9j
complexNum2 = 9-9j
complexNum3 = -9j
complexNum4 = 9j

print(".....complex numbers demo.....")
print(complexNum1)
print(type(complexNum1))
print(complexNum2)
print(type(complexNum2))
print(complexNum3)
print(type(complexNum3))
print(complexNum4)
print(type(complexNum4))

#Type conversions : convert from one data type to other using the methods – int(), float() and complex()
intNum1 = 77
floatNum2 = 3.30

intToFloat = float(intNum1)
floatToInt = int(floatNum2)
intToComplex = complex(intNum1)

print("....type conversion demo....")
print(intToFloat)
print(type(intToFloat))
print(floatToInt)
print(type(floatToInt))
print(intToComplex)
print(type(intToComplex))

#create random number using random module
print("random numbers demo....")
import random
print(random.randrange(10, 20))