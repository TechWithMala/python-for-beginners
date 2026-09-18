#Lambda function demo...

#Syntax : lambda arguments: expression

#addition using lambda function
print("...#addition using lambda function...")
add = lambda arg1 : arg1 + 5
print(add(5))

#subtraction using lambda function
print("...#subtraction using lambda function...")
sub = lambda arg1 : arg1 - 5
print(sub(5))

#multiplication using lambda function
print("...#multiplication using lambda function...")
mul = lambda arg1, arg2 : arg1*arg2
print(mul(5, 5)) #notice we are passing more than one argument

#division using lambda function
print("...#division using lambda function...")
div = lambda arg1, arg2, arg3 : arg1/arg2/arg3
print(div(500, 50, 5)) #notice we are passing more than one argument

##using lambda function inside another function
print("...#using lambda function inside another function...")
def function1(t):
    return lambda arg1 : arg1 * t

doubleTheNumberPassed = function1(2)
tripleTheNumberPassed = function1(3)

print(doubleTheNumberPassed(10))
print(tripleTheNumberPassed(10))