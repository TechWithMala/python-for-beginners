#If else statements demo...

#write if statement by using the "if" keyword
print("...write if statement by using the \"if\" keyword...")

johnAge = 40
bobsAge = 43
if bobsAge > johnAge:
    print("Bob is elder than John")

#write elif statement using "elif" keyword, this will be executed if the prior condition fails to execute
johnAge = 40
bobsAge = 40
print("...write elif statement using \"elif\" keyword...")
if bobsAge > johnAge:
    print("Bob is elder than John")
elif bobsAge == johnAge:
    print("John and Bob are equal in age")

#write else statement by using "else" keyword and will be executed when the prior conditions fail to catch any
johnAge = 45
bobsAge = 40
print("...write else statement by using \"else\" keyword...")
if bobsAge > johnAge:
    print("Bob is elder than John")
elif bobsAge == johnAge:
    print("John and Bob are equal in age")
else:
    print("John is elder than Bob")

#else without an elif
johnAge = 45
bobsAge = 40
print("...else without an elif...")
if bobsAge > johnAge:
    print("Bob is elder than John")
else:
    print("John is elder than Bob")

#use "short hand if" when we have only one statement to execute
johnAge = 40
bobsAge = 43
print("...use short hand if...")
if bobsAge > johnAge: print("Bob is elder than John")

#use "Short Hand If Else" when we have only one statement to execute in both if and else
johnAge = 45
bobsAge = 43
print("...Short Hand If Else...")
print("Bob is elder than John") if bobsAge > johnAge else print("John is elder than Bob")

#multiple else statements in one line
johnAge = 43
bobsAge = 43
print("...multiple else statements in one line...")
print("John is elder than Bob") if johnAge > bobsAge else print("John and Bob are equal in age") if johnAge == bobsAge else print("Bob is elder than John")

#use 'and' and 'or' keyword to combine conditional statements
johnAge = 43
bobsAge = 23
chrisAge = 58
print("...use 'and' keyword to combine conditional statements...")
if johnAge > bobsAge and chrisAge > johnAge:
    print("the above conditional statements are true...")

print("...use 'or' keyword to combine conditional statements...")
if bobsAge > johnAge or chrisAge > johnAge:
    print("at least one of the conditions from the above is true...")

#Nested If - if statements inside if statements
johnAge = 43

print("...Nested If...")
if johnAge > 20:
    print("John is above 20....")
    if johnAge > 30 :
        print("and also John is above 30...")
    else:
        print("John is not above 30...")

#use 'pass' statement when we have empty if statements
johnAge = 43
bobsAge = 23

print("...use 'pass' statement...")
if johnAge > bobsAge: #w/o pass : SyntaxError: unexpected EOF while parsing
    pass