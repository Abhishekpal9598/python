# # import pyjokes
# joke=pyjokes.get_joke()
# print(joke)

# import pyjokes

# # joke=pyjokes.get_joke()
# # print(joke)

# ######## print poem of twinkle twinkle

# print('''Twinkle twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.''')


## use repl and print the table of 5

# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.

# Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

# PS C:\Users\Abhishek Pal> python
# Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> for i in range(1,n+1)
#   File "<stdin>", line 1
 
#                          ^
# SyntaxError: expected ':'
# >>> 5*1
# 5
# >>> 5*2
# 10
# >>> 5*3
# 15
# >>> 5*4
# 20
# >>>



# install an external module of  your interest
#engine.say("I will speak this text")
# engine.runAndWait()

#mport pyttsx3
#engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

#engine.say("I will speak this text")
#engine.runAndWait()

##wap contents of a directory using the os module

# import os

# # Get the path of the directory
# directory = input("Enter the directory path: ")

# try:
#     # List all files and folders in the directory
#     contents = os.listdir(directory)

#     print(f"\nContents of '{directory}':")
#     for item in contents:
#         print(item)

# except FileNotFoundError:
#     print("The directory does not exist.")
# except PermissionError:
#     print("You don't have permission to access this directory.")


#
# l1=[23,4,2,324,2,42]
# print(sum(l1))
#jokes = pyjokes.get_jokes(language="en", category="neutral")
#for j in jokes[:5]:   # printing first 5 jokes
  #  print(j)
# mini project: Joke Teller
import pyjokes
import time

print("😂 Welcome to the Python Joke Teller! 😂")
print("----------------------------------------")

# ask user how many jokes they want
try:
    num = int(input("How many jokes do you want to hear? "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# fetch jokes
jokes = pyjokes.get_jokes(language="en", category="neutral")

# show jokes one by one
for i in range(min(num, len(jokes))):
    print(f"\nJoke {i+1}: {jokes[i]}")
    time.sleep(2)  # wait 2 seconds before next joke

print("\nThat's all the jokes for now! 🤣")
