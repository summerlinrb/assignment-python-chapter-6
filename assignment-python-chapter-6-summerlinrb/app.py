# Watching the short videos at codewithmosh.com is very important for
# understanding this chapter
from timeit import timeit

# Chapter 6.1 Exceptions
# nothing to code. Watch the video


# Chapter 6.2 Handling Exceptions
print("\nChapter 6.2 Handling Exceptions")
print("\nTo test the erorrs, enter correct and bad values for age('z', -1, etc.)")
# Run "python app.py" or "python3 app.py" in the terminal to allow for user input

# Start coding here...
# Brandon Summerlin

# basic error handling
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# setting variable as error and printing the error
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# 6.3 Handling Different Exceptions
print("\nChapter 6.3 Handling different exceptions")
# try inputting 0 as the age to see the message
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age must be greater than zero.")
else:
    print("No exceptions were thrown.")
print(xfactor)

# one except clause can handle multiple exceptions
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print(xfactor)

# Chapter 6.4 Cleaning Up
print("\nChapter 6.4 Cleaning Up")
# finally clause always runs whether there is an error or not
# useful for when opening a file and you need it closed regardless
# if theere is an error or not
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()

# Chapter 6.5 The With Statement
print("\nChapter 6.5 With Statement")
try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# Chapter 6.6 Raising Exceptions
print("\nChapter 6.6 Raising Exceptions")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
    # notice the variable "error"
    # it holds info about the exception. the variable name can be any name you desire.
except ValueError as error:
    print(error)


# chapter 6.7 cost of raising exceptions
print("\nChapter 6.7 Cost of Raising Exceptions")
# as best practice - avoid raising exceptions where possible
# and instead use an if statement

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code = ", timeit(code1, number=10000))
print("second code = ", timeit(code2, number=10000))
