#for loop demo...

#for loop is used to iterate a sequence, example a string, list, set, dictionary, tuple

#loop through a list using for loop
print("...loop through a list using for loop...")
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for weekDay in weekDays:
    print(weekDay)

#loop through a string using for loop
print("...loop through a string using for loop...")
for lang in "python":
    print(lang)

#use break statement to stop the execution of the loop before it reaches all the elements
print("...use break statement to stop the execution of the loop before it reaches all the elements...")
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for weekDay in weekDays:
    print(weekDay)
    if weekDay == "Wednesday":
        break

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for weekDay in weekDays:
    if weekDay == "Wednesday":
        break
    print(weekDay)

#use 'continue' statement to stop the current iteration and continue with the next
print("...use 'continue' statement to stop the current iteration and continue with the next...")
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for weekDay in weekDays:
    if weekDay == "Wednesday":
        continue
    print(weekDay)

#use 'range()' function to loop through the code by a specified number of times
print("...use 'range()' function to loop through the code by a specified number of times...")
for weekDays in range(5):
    print(weekDays) #notice the index starts from 0

#add parameter to specify the starting value of the index for range() function
print("...add parameter to specify the starting value of the index for range() function...")
for weekDays in range(2, 4):
    print(weekDays) #notice the index 4 is excluded

#by default the sequence gets incremented by 1, use third parameter to specify the increment value
print("...by default the sequence gets incremented by 1, use third parameter to specify the increment value...")
for weekDays in range(1, 5, 2):
    print(weekDays)

#use 'else' in for loop to execute a block of code when the for loop completes execution
print("..use 'else' in for loop to execute a block of code when the for loop completes execution..")
for weekDays in range(5):
    print(weekDays)
else:
    print("not in the for loop...")

#use nested loops to specify loop inside a loop
print("...use nested loops to specify loop inside a loop...")
numbersList = [1, 2, 3, 4, 5]
alphabetList = ['x', 'y', 'z']
for number in numbersList:
    print(number)
    for alphabet in alphabetList: #inner loop gets executed for each iteration of the outer loop
        print(alphabet)

#use pass statement when we have empty for loop
print("...use pass statement when we have empty for loop...")
numbersList = [1, 2, 3, 4, 5]
for number in numbersList:
    pass