#     * ASCII Codes Overview
# ASCII (American Standard Code for Information Interchange) is a character encoding standard used to represent text in computers and other devices.
# Each character is assigned a unique numerical value, known as its ASCII code.

#     * ASCII Code Ranges in the Code
# Uppercase Letters (A-Z): ASCII codes 65 to 90.
# Lowercase Letters (a-z): ASCII codes 97 to 122.
# Digits (0-9): ASCII codes 48 to 57.

#     * Code Breakdown
# Printing Uppercase Letters (A-Z):
#   python
#   for i in range(65, 91):
#       print(chr(i))
  
#  This loop iterates through ASCII codes 65 to 90 and prints the corresponding uppercase letters.

# Printing Lowercase Letters (a-z):
#   python
#   for i in range(97, 123):
#       print(chr(i))
  
#  This loop iterates through ASCII codes 97 to 122 and prints the corresponding lowercase letters.

# Printing Digits (0-9):
#   python
#   for i in range(48, 58):
#       print(chr(i))
  
#  This loop iterates through ASCII codes 48 to 57 and prints the corresponding digits.

# Printing Uppercase Letter Patterns:
#   python
#   n = 5
#   for i in range(n):
#       for j in range(i+1):
#           print(chr(65+i), end=" ")
#       print()
  
#  This nested loop prints a pattern of uppercase letters, where each row contains the same letter repeated based on the row number.

# Printing Lowercase Letter Patterns:
#   python
#   n = 5
#   for i in range(n):
#       for j in range(i+1):
#           print(chr(97+i), end=" ")
#       print()
  
#  This nested loop prints a pattern of lowercase letters, similar to the uppercase pattern.

# Printing Digit Patterns:
#   python
#   n = 5
#   for i in range(n):
#       for j in range(i+1):
#           print(chr(48+i), end=" ")
#       print()
  
#  This nested loop prints a pattern of digits, similar to the letter patterns.

#     * Output Summary
# The code prints:
#  All uppercase letters (A-Z).
#  All lowercase letters (a-z).
#  All digits (0-9).
#  Patterns using uppercase letters, lowercase letters, and digits.

# This code effectively demonstrates the use of ASCII codes to generate and print characters and patterns.







# for i in range(65, 91):
#     print(chr(i))

# for i in range(97, 123):
#     print(chr(i))

# for i in range(48, 58):
#     print(chr(i))

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(97+i), end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(48+i), end=" ")
#     print()