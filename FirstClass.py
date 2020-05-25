# My name is Benjamin C.
# Written on 25th may 2020
# First class in Day 2

# name = "ChisoftMedia"

# print("My name is " + name)
# print("Thank you")

# Indentation
# a = 10
# b = 0
# if (a == b):
#    print("a equals b")
# else:
#    print("a is not equal to b")

# Multi-line Statements in Python
# title = "Mr. "
# firstname = "Benjamin "
# lastname = "Chinwe "
# othername = "Uchenna "
# fullname = title + \
#            firstname + \
#            lastname + \
#            othername
# print(fullname)

# myName = input("Please enter your name? ")
# if not myName:
#     myName = input("Please you need to enter your name? ")

# if myName:
#    print("Your name is: " + myName)


# Integer and string Data Type
# number1 = input("Please enter a first number :")
# number2 = input("Please enter a second number :")

# sum = int(number1) + int(number2)

# print("The sum of "+ number1 + " and " + number2 + " = " + str(sum))
# print(sum)


# Float and string Data Type
# number1 = input("Please enter a first score :")
# number2 = input("Please enter a second score :")

# sum = float(number1) + float(number2)

# print("The sum of "+ number1 + " and " + number2 + " = " + str(sum))
# print(sum)


# Multiple Assignments
x = y = 34
z = 41
math101 = eng101 =  54.9
chem101 = 61.9

name, score, age = "ChisoftMedia", ((float(math101)+float(eng101)+float(chem101))/3), ((int(x)+int(y)+int(z))/3)

print(name + "is Aged = " + str(age) + " and scored = " + str(score))