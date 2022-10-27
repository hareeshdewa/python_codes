#Bro code - Python tutorial:
#Day-1:
"""
#user input
name =input("What is your name?:")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello" + name)
print("You are "+ str(age) + " years old")
print("You are " + str(height) + "cm tall")
"""

#useful functions in math:
import math
pi = 3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))  #round the number up
print(math.floor(pi)) # round the number down
print(abs(pi))  #aboslute number
print(pow(pi, 2)) #power- will raise the base number to power
print(math.sqrt(23)) # random number which squares it.
print(max(x,y,z))
print(min(x,y,z))
print("\n")

#String slicing
#Slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]
name = "Hareesh Dewa"

first_name = name[0:3] # or [:3] are the same
last_name = name[4:8]
funky_name = name[::-1] # reverse the name
print(first_name)
print(last_name)
print(funky_name)

website ="http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website[slice])
print(website2[slice])
print("\n")

#if,elif and else statement:
"""
age = int(input("How old are you?: "))
if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
"""

#logical operator:
#logical operators (and,or,not) = used to check if two or
# more conditional statements is true
"""
temp = int(input("what is the temperature outside?: "))

if not(temp >=0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")

elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")
"""
#while loops:
#it is statement that will execute it's block of code
# as long as it's condition remains true
"""
name = ""
while len(name ) == 0:
    name = input("Enter your name: ")
print("Hello " + name)
#or 
name1 = None
while not name1:
    name1 = input("Enter your name: ")
print("Welcome, " + name1)
"""
#For loop:
# A statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

"""
for i in range(10):
    print(i) # starts from 0 and ends at 9
    print("\n")

for n in range(50,100+1, 2):
    print(n)
print("\n")

for a in "Hareesh Dewa":
     print(a)
print("\n")

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New year!")
"""
#Nested loops:
# A general concept of having one lopp inside another loop
"""
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol =  input("Enter the symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
"""
print("\n")

#Loop control statment:
#break -  used to terminate the loop entirely
# continue - skips to the next iteration of the loop
# pass -  does nothing, acts as a placeholder
"""
while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i =="-":
        continue
    print(i,end="")
print("\n")

for j in range(1,21):
    if j == 13:
        pass
    else:
        print(j)
"""

#list =  used to store multiple items in a simgle variable

food = ["pizza","hamburger","Biriyani", "Noodles","cake"]
food[0] = "Sushi"
food.append("Ice cream")
food.remove("cake")
food.pop()
food.insert(0,"Donut")
food.sort()

for x in food:
    print(x)
print("\n")


#2D list = a list of lists
drinks = ["milkshake", "soda", "tea"]
dinner = ["pongal", "idli", "Dosa"]
dessert = ["Ice cream", "Donut", "Cake"]
foods = [drinks,dinner,dessert]
print(foods[2][2])
print("\n")

#Day-2:
#Tuple:
#collection which is ordered and unchangeable used to group together related data

student = ("Bro",21,"male")
print(student.count("Bro"))
print(student.index("male"))
for x in student:
    print(x)
if "Bro" in student:
    print("Bro is here!")
print("\n")

#Set:
#collection which is unordered,unindexed. No duplicate values

kitchen = {"fork", "spoon", "knife","spoon"}
dishes = {"bowl", "plate", "cup","knife"}
#add an item
kitchen.add("napkin")
kitchen.remove("spoon")
#kitchen.update(dishes)
# dishes.update(kitchen)
dinner_table = kitchen.union(dishes)
print(kitchen.difference(dishes)) # unsimilarity strings
print(kitchen.intersection(dishes)) #common string from the sets
for y in kitchen:
    print(y)
print("\n")

#Dictionary:
# An unchangeable , unordered collection of unique key:values pairs
# fast because they use hasing, allows us to access a value quickly
#mutable

capitals = {"USA": "washington",
            "India":"Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
print(capitals["Russia"])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
for key,value in capitals.items():
    print(key,value)
print("\n")

#index operator:
#gives access to a sequence's element (Str,list,tuples)
letter = "Hareesh Dewa!"
if letter[0].islower():
    letter = letter.capitalize()
print(letter)

firstname = letter[0:7].upper()
lastname = letter[8:].lower()
last_character = letter[-1]
print(firstname)
print(lastname)
print(last_character)
print("\n")

#functions:
#a block of code which is executed only when it is called
def hello(firstname,lastname,age):
    print("Hello! " + firstname + " " + lastname)
    print("You are " + str(age) +" years old!")
    print("Have a nice day!")
hello("Hareesh","Dewa",20)
print("\n")

#return Statement:
#functions send python values/objects back to the caller.
#These values/objects are known as the function's return value.

def multiple(num1, num2):
    result = num1 * num2
    return result
#or return num1 * num2
#print(multiple(6,8)) # return statement comes under print
x = multiple(6,8)
print(x)
print("\n")

#keyword arguements:
#arguments proceeded  by an identifier when we pass them to a function
#The order of the argument doesn't matter, unlike positional arguments
#python knows the name of the arguments that our function receives.

def hello(first,middle,last):
    print("Hello " +first+" "+middle+" "+last)
hello(last="Code",middle="Dude",first="Bro")
print("\n")

#nested function call:
"""
function calls inside other function calls
innermost function calls are resolved first
returned values is used as arguments for the next other functions

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num) - absolute number
num = round(num)
print(num) 
in order to do this, we can make sure like:
"""
#print(round(abs(float(input("Enter a whole positive number: ")))))

#scope:
# The region that a variable is recognized
# A variable is only available from inside the region it is created
# A global and locally scoped version of a variable can be created

name = "Hareesh" #global scope (available inside and outside)
def display_name():
    name = "Dewa" # local scope (available only inside this function)
    print(name)

print(name)
display_name()
print("\n")

# *args:
"""
Parameter that will pack all arguments into a tuple
useful so that a function can accept a varying amount of arguments
def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(1,2))
"""
def add(*stuff): #packing them into tuple
    # *args can be changed into any names of a string
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum = sum + i
    return sum

print(add(1,2,3,4,5,6))
print("\n")

#**kwargs:
"""
parameter that will pack all the arguments into a dictionary 
useful so that a function can accept a varying amount of keyword arguments
"""
def hello(**kwargs):
    # print("Hello "+ kwargs['first'] +" " + kwargs['last'])
    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.",first="Hareesh", middle="Dude",last="Dewa")
print("\n")

#str.format()
"""
optional method that gives users more control when displaying output
"""
animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the " + item)
print("The {} jumped over {}".format(animal,item))
print("The {1} jumped over {0}".format(animal,item)) #positinal argument
print("The {item} jumped over {item}".format(animal="cow",item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

name1 = "Hareesh"
print("Hello, my name is {:10}.Nice to meet you".format(name1)) #spacing
print("Hello, my name is {:<10}.Nice to meet you".format(name1)) #spacing
print("Hello, my name is {:>10}.Nice to meet you".format(name1)) #left align
print("Hello, my name is {:^10}.Nice to meet you".format(name1)) #center align

number = 1000

print("The number pi is {:.3f}".format(number)) #first two digits after decimals
print("The number is {:,}".format(number)) #thousands
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number)) #octal
print("The number is {:X}".format(number)) #hexadecimal
print("The number is {:E}".format(number)) #uppercase or e- lowercase
print("\n")

#Day-3:
#random:
#Pseudo

import random
x = random.randint(1,6) # random integer
y = random.random() # picks up some random

mylist = ['rock','paper','scissors']
z = random.choice(mylist) # decides as its own way to choose
cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards) #shuffles
print(cards)
print(z)
print(y)
print(x)
print("\n")

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
#File detection:
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

#File-Read





