# My name is Benjamin C.
# Written on 25th may 2020
# First class in Day 2

name = "ChisoftMedia"

print("My name is " + name)
print("Thank you")

# Indentation
a = 10
b = 0
if (a == b):
   print("a equals b")
else:
   print("a is not equal to b")

# Multi-line Statements in Python
title = "Mr. "
firstname = "Benjamin "
lastname = "Chinwe "
othername = "Uchenna "
fullname = title + \
           firstname + \
           lastname + \
           othername
print(fullname)

myName = input("Please enter your name? ")
if not myName:
    myName = input("Please you need to enter your name? ")

if myName:
    print("Your name is: " + myName)