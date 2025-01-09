# Functions
# ................................................................................
# ...................non-return and non-argument function.........................
# ................................................................................

# Sum of two number:
# def sum():
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     sum = a + b
#     print("Sum of a and b is: ", sum)

# sum()



# ................................................................................
# .......................non-return and argument function.........................
# ................................................................................
# def interest(a,b,c):
#     simple_interest = (a * b * c) / 100
#     total_amount = a + simple_interest

#     print("Simple Interest: ", simple_interest)
#     print("Total Amount: ", total_amount)

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate: "))
# time = float(input("Enter the time period in years: "))

# interest(principal, rate, time)


# ......................................................................................
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# # Upper part of hollow diamond
# def diamond(row):
#     for i in range(1, row+1):
#         for j in range(1,row-i+1):
#             print(" ", end="")
#         for j in range(1, 2*i):
#             if j==1 or j==2*i-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# # Lower part of hollow diamond
#     for i in range(row-1,0, -1):
#         for j in range(1,row-i+1):
#             print(" ", end="")
#         for j in range(1, 2*i):
#             if j==1 or j==2*i-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# row = int(input("Enter rows: "))
# diamond(row)



# ................................................................................
# .......................return and non-argument function.........................
# ................................................................................
# sum of all natural number
# def sum():
#     m = int(input("Enter the value of m: "))
#     n = int(input("Enter the value of n: "))
#     sum = 0
#     for i in range(m, n+1):
#         sum += i
#     return sum

# res = sum()
# print(res)



# ................................................................................
# .......................return and argument function.............................
# ................................................................................

# def sum(a,b):
#     sum = 0
#     for i in range(m, n+1):
#         sum = sum + i
#     return sum

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))

# print(sum(m,n))

# j = int(input("Enter the value of m: "))
# p = int(input("Enter the value of n: "))

# print(sum(j,p))



# ................................................................................
# leap year by all type functions

# non-return and non-argument function

# def leap():
#     year = int(input("Enter a year.."))
#     if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(year, "is a leap year.")
#     else:
#         print(year, "is not leap year.")
# leap()


# return and non-argument function

# def leap():
#     year = int(input("Enter a year.."))
#     if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return print(year, "is a leap year.")
#     else:
#         return print(year, "is not leap year.")

# leap()


# non-return and argument function

# def leap(year):
#     if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(year, "is a leap year.")
#     else:
#         print(year, "is not leap year.")

# year = int(input("Enter a year.."))
# leap(year)


# return and argument function

# def leap(year):
#     if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return print(year, "is a leap year.")
#     else:
#         return (year, "is not leap year.")

# year = int(input("Enter a year.."))
# leap(year)




# ................................................................................
# ..........Examples......Examples........Examples................................

# 50 basic programming problems focused on functions:

# 1. Write a function to sum of m to n numbers.
# def sum():
#     sum = 0
#     for i in range (m, n+1):
#         sum += i
#     return sum

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))

# res = sum()
# print(res)


# 2. Write a function to return the square of m to n number.
# def square():
#     for i in range (m, n+1):
#         square = 0l
#         square = i * i
#         print(f"{i}² = {square}")

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))

# res = square()
# print(res)


# 3. Write a function to find the average of n numbers.(using for and while loop)

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))
# def average():
#     count = 0
#     sum = 0
#     for i in range (m, n+1):
#         sum += i
#         count += 1
#     avg = sum / count
#     return avg

# print(average())

# 4. Write a function to check if a number is even or odd and +ve or -ve in less code.
# def check():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0 and num < 0:
#         print(f"{num} is a negative even number.")
#     elif num % 2 == 0 and num > 0:
#         print(f"{num} is a positive even number.")
#     elif num % 2 != 0 and num < 0:
#         print(f"{num} is a negative odd number.")
#     elif num % 2 != 0 and num > 0:
#         print(f"{num} is a positive odd number.")
#     else:
#         print("Zero number")

# check()


# Extra.:- Write a function to find the factorial of a number using recursion.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


# 5. Write a function to calculate the factorial of given number.
# def fact():
#     num = 1
#     for i in range (2, n+1):
#         num = num * i
#     return num


# n = int(input("Enter the value of n: "))

# res = fact()
# print(f" factorial of {n} is {res}")



# 6. Write a function to find the greatest common divisor (GCD) of two numbers.
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# print(gcd(a,b))

# .........OR......
# import math
# def gcd(a, b):
#   return math.gcd(a, b)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = gcd(num1, num2)
# print(f"The GCD of {num1} and {num2} is {result}")



# 7. Write a function to find the least common multiple (LCM) of two numbers.
# def lcm(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
#     while(True):
#         if((greater % a == 0) and (greater % b == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(lcm(num1, num2))

# .........OR......
# import math
# def lcm(a, b):
#     return a * b // math.gcd(a, b)
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = lcm(num1, num2)
# print(f"The LCM of {num1} and {num2} is {result}")



# 8. Write a function to check if a number is prime.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1): # loop run till sqrt of n(half of it)
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")




# 9. Write a function to generate a list of prime numbers up to a given limit.

# def prime_num(num):
#     prime  = []

#     for nums in range(2, num):
#         is_prime = True
#         for i in range(2, int(nums ** 0.5) + 1):
#             if nums % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(nums)
#     return prime
            
# num = int(input("Enter a number: "))
# print(prime_num(num))


# 10. Write a function to reverse a string.

# def reverse_string(s):
#     return s[::-1]
# s = input("Enter a string: ")
# print(reverse_string(s))



# 11. Write a function to check if a string is a palindrome.

# def reverse_string():
#     s = input("Enter a string: ")
#     if s == s[::-1]:
#         print(f"{s} is palindrome ")
#     else:
#         print(f"{s} is not palindrome ")

# print(reverse_string())



# 12. Write a function to count the number of vowels in a string.
# def vowels(s):
#     count = 0
#     for char in s:
#         if char.lower() in 'aeiou':
#             count += 1
#         else:
#             print("no vowels in string")
#     return count
# s = input("Enter a string: ")
# print(vowels(s))



# 14. Write a function to find the average of numbers in a list.

# 15. Write a function to find the maximum value in a list.

# 16. Write a function to find the minimum value in a list.

# 17. Write a function to count the occurrences of an element in a list.
# 18. Write a function to remove duplicates from a list.
# 19. Write a function to check if an element is present in a list.
# 20. Write a function to merge two lists into one.
# 21. Write a function to find the intersection of two lists.
# 22. Write a function to find the union of two lists.
# 23. Write a function to count the number of words in a sentence.
# 24. Write a function to calculate the sum of the first `n` natural numbers.
# 25. Write a function to generate the Fibonacci series up to `n` terms.
# 26. Write a function to find the nth Fibonacci number using recursion.
# 27. Write a function to find the length of a list without using `len()`.
# 28. Write a function to convert a string to lowercase.
# 29. Write a function to convert a string to uppercase.
# 30. Write a function to convert a temperature from Celsius to Fahrenheit.
# 31. Write a function to convert a temperature from Fahrenheit to Celsius.
# 32. Write a function to swap two numbers.
# 33. Write a function to check if a year is a leap year.
# 34. Write a function to calculate the area of a circle given its radius.
# 35. Write a function to calculate the perimeter of a rectangle.
# 36. Write a function to calculate the area of a triangle given its base and height.
# 37. Write a function to check if a number is a perfect square.
# 38. Write a function to find the sum of the digits of a number.
# 39. Write a function to check if two strings are anagrams.
# 40. Write a function to calculate the power of a number (`base^exponent`).
# 41. Write a function to find the smallest divisor of a number greater than 1.
# 42. Writ,e a function to calculate the sum of all even numbers in a list.
# 43. Write a function to find the longest word in a sentence.
# 44. Write a function to count the frequency of each character in a string.
# 45. Write a function to check if a list is sorted in ascending order.
# 46. Write a function to sort a list in descending order.
# 47. Write a function to find the second largest number in a list.
# 48. Write a function to remove all occurrences of a specific element from a list.
# 49. Write a function to calculate the compound interest given principal, rate, and time.
# 50. Write a function to print a multiplication table for a given number.


# --------------------------------------------------------------
# ..........Lambda Function......................
# --------------------------------------------------------------
# lambda function


# add two numbers
# add = lambda x,y : x + y
# print(add(4,6)) # output: 10


# square a number
# square = lambda x : x * x
# print(square(4)) # output: 16


# num is even or odd
# res = lambda a: a % 2 == 0
# num = int(input("Enter num: "))
# print(res(num)) # True or false



# sum = lambda x,y : (x+y)
# print(sum(5,6))

# --------------------------------------------------------------
# ..........Lambda Function End......................
# --------------------------------------------------------------

# sum of any n digit number
# def number():
#     num = int(input("Enter a n digit number: "))
#     sum = 0
#     count = 0
#     b = len(str(num))
#     while count < b+1:
#         r = int(num % 10)
#         num = int(num / 10)
#         sum = sum + r
#         count += 1
#     print(sum)

# number()



# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# output should: [8,9,9,9,0,0,0,1]





# .....................multiple argumente in 1 functions........................
# .....................multiple argumente in 1 functions........................
# .....................multiple argumente in 1 functions........................


# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# add(5,6,7,8,9)


# .........passing list as an argument...................
# .........passing list as an argument...................
# def add(li):
#     sum = 0
#     for i in li:
#         sum = sum + i
#     print(sum)
    
# def getnum():
#     count = int(input("How many numbers you want to add: "))
#     li = []
#     for i in range(0,count):
#         num = int(input("Enter a number: "))
#         li.append(num)
#     return li

# li = getnum()
# add(li)


def oddeven(m,n):
    flag1 = 0
    flag2 = 0
    odd = []
    even = []
    for num in range(m,n+1):
        if num % 2 == 0:
            even.append(num)
            flag1+= 1
        else:
            odd.append(num)
            flag2+=1
    print(f"totle {flag1} of even nums are: {even}")    
    print(f"totle {flag2} of odd nums are: {odd}")

m = int(input("Enter m: ")) 
n = int(input("Enter n: "))
oddeven(m,n) 
