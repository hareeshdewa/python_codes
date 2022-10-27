#exception:
# events detected during execution that interrupt the flow of program.
"""
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: # e- optional
    print(e)
    print("You can't divide by zero! idiot!")

except ValueError as e:
    print(e)
    print("Enter only number plz!")

except Exception as e:
    print(e)
    print("Something went wrong :( ")

else:
    print(result)

finally:
    print("This will always execute")
print("\n")
"""
"""
#File detection: to check whether the folder/file  has existed.
import os
path = "C:\\Users\\User\\OneDrive\\Desktop\\folder"
if os.path.exists(path):
    print("That Location exists!")
    if os.path.isfile(path): #text document
        print("That is a file ")
    elif os.path.isdir(path): #folder
        print("That is a directory!")
else:
    print("That location doesn't exist!")
print("\n")

#File-Read
try:
    with open('text.txt') as file:
      print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#File-write
#text ="Have a nice day!\n" #execute first at w

# r- read
# w- write
# a - append

with open('test.txt','a') as file:
    file.write(text)


#copyfile():

copies content of a file
copy() - copyfile() + permission mode + destination can be directory
copy2() - copy() + copies metadata(file's creation and motification time)
everything does the same exact arguments


#importing copy from shutil

import shutil

shutil.copyfile('test.txt','C:\\Users\\User\\OneDrive\\Desktop\\copy.txt') #src,dst
"""
print("\n")
"""
#move file:
import os
folder_name = "folder"
destination = "C:\\Users\\User\\OneDrive\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(folder_name,destination)
        print(folder_name +" was moved")
except FileNotFoundError:
    print(folder_name + " was not found")

print("\n")
"""
"""
import os
import shutil

path = 'folder'
try:
    #os.remove(path) #-to delete a file
    #os.rmdir(path) -to delete the folder from the directory
    #shutil.rmtree(path) # to delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path +" was deleted")
"""
