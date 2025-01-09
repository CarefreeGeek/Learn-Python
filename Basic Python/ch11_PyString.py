# -----------------------------------------------------------------------
# --------------------Theories-------------------------------------------
# -----------------------------------------------------------------------
# date 25-09-2024


# characteristics of strings

# Here's a comprehensive guide to string manipulation in Python:
# ------------------Basic String Methods---------------------------
# capitalize the first letter
# str="this is the data"
# print(str.capitalize())

# case fold convert all the data into lower case
# str="This is the data"
# print(str.casefold())

# center string
# str="this is the data"
# print(str.center(40))

# str="this is the data"
# print(str.center(40,'$'))

# count the occurrence of the word
# str="this is the data"
# print(str.count("is"))

# check the ending pf the data
# str="this is the data"
# print(str.endswith("data"))

# //wap to encode the DeprecationWarning
# str="this is the data"
# print(str.encode())

# find the data
# str="this is the data"
# print(str.find("is"))


# index the data
# str="this is the data"
# print(str.index("the"))

# str="this56"
# print(str.isalnum())
# print(str.isalpha())
# print(str.isascii())
# print(str.isdigit())
# print(str.isdecimal())


# replace the data
# str="this is the data"
# print(str.replace("is","are"))


# upper case
# str="this is the data"
# print(str.upper())
# print(str.lower())

# join the data
# str=("Rowan","moham","menu")
# print("$".join(str))

# wap to remove the extra space from the string
# str="    this is the data  "
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())

# =======================================

# String Operations:

# 1. Concatenation: +
#     - Example: "Hello, " + "World!"

# 2. Repetition: *
#     - Example: "Hello" * 3

# 3. Indexing: []
#     - Example: "Hello"[0] returns "H"

# 4. Slicing: [:]
#     - Example: "Hello"[1:4] returns "ell"

# 5. Length: len()
#     - Example: len("Hello") returns 5


# String Methods:

# 1. upper(): Returns uppercase string
#     - Example: "hello".upper() returns "HELLO"

# 2. lower(): Returns lowercase string
#     - Example: "HELLO".lower() returns "hello"

# 3. strip(): Removes leading/trailing whitespace
#     - Example: " Hello ".strip() returns "Hello"

# 4. split(): Splits string into list
#     - Example: "hello world".split() returns ["hello", "world"]

# 5. join(): Joins list into string
#     - Example: "-".join(["hello", "world"]) returns "hello-world"

# 6. replace(): Replaces substring
#     - Example: "hello world".replace("world", "Python") returns "hello Python"

# 7. find(): Returns index of substring
#     - Example: "hello world".find("world") returns 6

# # 8. count(): Returns count of substring
# #     - Example: "hello world".count("l") returns 3


# # Regular Expressions (regex):

# # 1. Import re module
# # 2. Use re.search(), re.match(), re.findall() for pattern matching


# Example Code:

# String operations
# name = "John Doe"
# print(name.upper())  # JOHN DOE
# print(name.split())  # ["John", "Doe"]
# print("-".join(name.split()))  # John-Doe

# String methods
# text = "   Hello, World!   "
# print(text.strip())  # Hello, World!
# print(text.replace("World", "Python"))  # Hello, Python!

# # Regex example
# import re
# text = "My phone number is 123-456-7890"
# pattern = r"\d{3}-\d{3}-\d{4}" # search the specific pattern string
# match = re.search(pattern, text)
# print(match.group())  # 123-456-7890



# This covers the basics and beyond of string manipulation in Python
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Q.1- Write a program to find top two maximum numbers in an array?
# def max_two():
#     max1 = 0     # initialize that two nums 
#     max2 = 0
#     for x in nums:     # run the loop in the list/array
#         if max1 < x:     # compare if max1 is < elements then assign max1 to max2 and n to max1
#             max2 = max1
#             max1 = x
#         elif max2 < x:     # if max2 < n then assign  max2 = n
#             max2 = x
#     print(f"first maximum num is {max1}")
#     print(f"second maximum num is {max2}")

# nums = [5,34,78,2,45,1,99,23]
# max_two()



# Q.2- Write a program to count all vowels in a string
# count= 0
# string = str.lower(input("Enter string: "))
# vowel =str("aeiou")
# for x in string:
#     for y in vowel:
#         if x == y:
#             count += 1
# print(count)



# Q.3- Write a program to check if a string is palindrome or not
# def palindrome():
#     s1 = str.lower(input("Enter string: "))
#     for x in range(len(s1)+1,1,-1):
#         s2 = s1[::-1]
#     if s1 == s2:
#         print(f"The string '{s1}' is palindrome")
#     else:
#         print(f"The string '{s1}' is not palindrome")

# palindrome()



# Q.4 Write a program count the words and spaces
# def count():
#     text = str(input("Enter string: "))
#     space = 0
#     char = 0
#     l = len(text)+1
#     for x in text:
#         if x == " ":
#             space += 1
#     words = text.split()
#     count = len(words)
#     print(f"In this string there are {space} spaces and {count} word.")

# count()



# Q.5 Write a program to print a to z capital and small
# for x in range (65,91):
#     print(chr(x), end=" ")
# print(" ")
# for y in range (97,123):
#     print(chr(y), end=" ")

# Q.6 Write a Python program to count the number of characters (character frequency) in a string.
# def count():
#     str1 = str(input("Enter string: "))
#     dict = {} # Retrieve the keys (unique characters) in the 'dict' dictionary.
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     print(dict)
# count()

# Q.7 Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# def res():
#     str1 = str(input("Enter string: "))
#     if len(str1) < 2:
#         print("")
#     else:
#         print(str1[0:2] + str1[-2:])

# res()


# Q.8 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to 'a symbol, except the first char itself.
# def replace():
#     str1 = str(input("Enter string: "))
#     char = str1[0]
#     str2 = str1.replace(char, '$')
#     res = char + str2[1:]
#     print(res)

# replace()


# Q.9 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. ie. 'abc','xyz' "res xyc abz"
# def uni():
#     str1 = str(input("Enter 1st string: "))
#     str2 = str(input("Enter 2nd string: "))
#     a1 = str1[0:2]
#     a2 = str2[0:2]
#     res = a2 + str1[2:] + " " + a1 + str2[2:]
#     print(res)

# uni()


# Q.10 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# def ing():
#     str1 = str(input("Enter string: "))
#     if len(str1) < 3:
#         print(str1)
#     else:
#         if str1[-3:] == "ing":
#             print(str1 + "ly")
#         else:
#             print(str1 + "ing")
# ing()


# Q.11 Write a Python program to remove the nth index character from a nonempty string.
# def nth():
#     text = str(input("Enter the string: "))
#     if len(text) > 1:
#         n = int(input("Enter the number to remove the character: "))
#         text = text.replace(text[n+1], "")
#         print(text)
#     else:
#         print("Very small string..")

# nth()


# Q.12  Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# def exch():
#     text = str(input("Enter the string: "))
#     n = len(text)
#     if len(text) >1:
#         indStart = text[0]
#         indLast = text[-1]
#         text2 = indLast + text[1:n-1] + indStart
#     print(text2)
# exch()


# Q.13  Write a Python program to remove characters that have odd index values in a given string.
# def oddStr(text):
#     res = ""
#     for x in range(len(text)):
#         if x % 2 == 0:
#             res = res + text[x]
#     return print(res)
# text = str(input("Enter the string: "))
# oddStr(text)


# Q.14  Write a Python program to count the occurrences of each word in a given sentence.
# def accrued(text):
#     dict = {} # Retrieve the keys (unique characters) in the 'dict' dictionary.
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     print(dict)

# str1 = str(input("Enter string: "))
# accrued(str1)



# Q.15 Write a Python program to find the number of occurrences of a given character in a string using a while loop.
# def repeatChar():
#     string = input("Enter string: ")
#     for x in range(65,123):
#         char = chr(x)
#         count = 0
#         i = 0
#         while i < len(string):
#             if string[i] == char:
#                 count += 1
#             i += 1
#         if count >= 1:
#             print(char,":", count, end=",    ")

# repeatChar()
        



# Q.16 Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# def sorting():
#     string = input("Enter string: ")
#     words = string.split()
#     res = sorted(words)
#     for x in res:
#         print(x, end=", ")

# sorting()


# Q.17 Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# def repLast():
#     text = str(input("Enter string: "))
#     if len(text) >= 2:
#         char = text[-2:]
#     print(char*4)

# repLast()


# Q.18 Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string. 
# def firstThree():
#     text = str(input("Enter string: "))
#     if len(text) >= 3:
#         word = text[:3]
#     print(word)

# firstThree()


# Q.19 Write a Python program to remove all vowels from a given string using a while loop.
# def remove():
#     string = input("Enter string: ")
#     vowels = "aeiouAEIOU"
#     i = 0
#     while i < len(string):
#         if string[i] in vowels:
#             string = string[:i] + string[i+1:]
#         else:
#             i += 1
#     print("String without vowels:", string)

# remove()


# Q.20  Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# def valid(text, minlength=8):
#     upper = False
#     lower = False
#     digit = False
#     for char in text:
#         if char.isupper():
#             upper = True
#         elif char.islower():
#             lower = True
#         elif char.isdigit():
#             digit = True
#     return len(text) >= minlength and upper and lower and digit

# print("Password must contains latter and digits")
# text = str(input("Enter string: "))
# if valid(text):
#     print("Password is valid..")
# else:
#     print("Does not meet requirements")