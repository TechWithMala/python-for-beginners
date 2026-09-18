# While loops demo...

#while loop can be used to execute a set of statements as long as the condition is true
print("...while loop...")
x = 3
while x < 7:
    print(x)
    x += 1 #increment x, else the loop runs forever

#use 'break' statement to stop execution even when the condition is true
print("...break statement...")
x = 3
while x < 7:
    print(x)
    if x == 5:
        break
    x += 1 #increment x, else the loop runs forever

#use 'continue' statement to stop the current iteration and continue with the next
print("...continue statement...")
x = 3
while x < 7:
    x += 1  # increment x, else the loop runs forever
    if x == 5:
        continue
    print(x)

#use 'else' statement to execute a block of code once when the condition is no longer true
print("else statement...")
x = 3
while x < 7:
    print(x)
    x += 1
else:
    print("x is not less than 7 anymore...")