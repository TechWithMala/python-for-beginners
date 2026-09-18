#File handling demo...

#file open using open() function
print("...file open using open() function...")
fOpen = open("fileHandling.txt") #Make sure file "fileHandling.txt" exists
#fOpen = open("fileHandling.txt", "rt") #readonly and text mode by default
print("file is opened...")

#read the content from the opened file using read() function
print("...read the content from the opened file using read() function...")
fOpenToRead = open("fileHandling.txt", "r") #open the file in read mode
print(fOpenToRead.read()) #returns the entire content from the file

#read-only specified characters from the file using the read() function
print("...read specified characters...")
fOpenToRead = open("fileHandling.txt", "r") #open the file in read mode
print(fOpenToRead.read(7)) #returns the first 7 characters

#read lines using readline() function
print("...read lines using readline() function...")
fOpenToRead = open("fileHandling.txt", "r") #open the file in read mode
print(fOpenToRead.readline()) #returns first line from the file

#read all the lines from the file by looping
print("...read all the lines from the file by looping...")
fOpenToRead = open("fileHandling.txt", "r") #open the file in read mode
for lines in fOpenToRead:
    print(lines)

#close file using close() function - good practice to close the opened resources/database connections
print("...close() function...")
fOpenToRead = open("fileHandling.txt", "r") #open the file in read mode
fOpenToRead.close()
print("file is closed...")

#write content to a file using write() function
print("...write content to a file using write() function, append mode...")
fOpenToWrite = open("fileHandling.txt", "a") #use a/w when opening a file to write content
fOpenToWrite.write("Newline has been added using append mode...")
fOpenToWrite.close()

#Now, read the added content from the file
print("...read after writing to a file using append mode...")
fOpenToWrite = open("fileHandling.txt", "r")
print(fOpenToWrite.read())

print("...write content to a file using write() function, write mode...")
fOpenToWrite = open("fileHandling.txt", "w")
fOpenToWrite.write("Newline has been added using write mode...") #overrides the entire content
fOpenToWrite.close()

#Now, read the added content from the file
print("...read after writing to a file using write mode...")
fOpenToWrite = open("fileHandling.txt", "r")
print(fOpenToWrite.read())

#delete a file using remove() function - BE CAREFUL WHEN RUNNING THIS...
#test data : create a new file - fileToRemove.txt
import os #imports os module
if os.path.exists("fileToRemove.txt"): #check if the file exists before deleting
    os.remove("fileToRemove.txt")
    print("file has been deleted...")
else:
    print("file doesn't exist...")

#delete an empty folder using rmdir() function
#test data : create a new folder - remove folder
import os
os.rmdir("remove folder")
print("folder has been deleted...")

