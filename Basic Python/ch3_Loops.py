# date 02-10-2024
# looping

# 1 to  100
# i = 1
# while i <=100:
#     print(i, end=" ")
#     i = i + 1


# a to z

#print 1 to 20 odd number
# i = 1
# while i <= 20:
#     if i % 2 !=0:
#         print(i)
#     i += 1

#print 1 to 20 even number
# i = 1
# while i <= 20:
#     if i % 2 ==0:
#         print(i)
#     i += 1
#===================================================================================
# Date 03-10-2024
#while loop


# print sum of all natural number from m to n
# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))
# sum = 0
# while m <= n:
#     sum = sum + m
#     m = m + 1
# print("Sum of all natural number from m to n is: ", sum)






# print all natural number from m to n with interval of 2
# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))
# while m <= n:
#     print(m, end="  ")
#     m = m + 1

#-----------------------------------------------------------------
# factorial of n number

# num = int(input("Enter a number: "))
# factorial = 1
# i = 1
# while i <= num:
#     factorial =factorial * i
#     i += 1
# print("Factorial of", num, "is", factorial)

#-----------------------------------------------------------------
# 2-Write a Python program to print the Fibonacci series up to a given number using a while loop.


# num = int(input("Enter a number: "))
# a, b = 0, 1
# count = 0
# while count < num:
#     print(a)
#     a, b = b, a + b
#     count += 1

#-----------------------------------------------------------------
# 3-Write a Python program to check if a given number is prime or not using a while loop.

# num = int(input("Enter a number: "))
# if num <= 1:
#     print(num, "is not a prime number")
# else:
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#         i += 1
#     else:
#         print(num, "is a prime number")

# 4-Write a Python program to reverse a string using a while loop.

# string1 = str(input("Enter your string/word: "))
# string2 = ""
# i = len(string1) - 1
# while i >= 0:
#     string2 += string1[i]
#     i -= 1
# print("Reversed string:", string2)

# 5-Write a Python program to find sum of m to n number and also print average of all number.

# m = int(input("Enter m"))
# n = int(input("Enter n"))
# count = 0
# sum = 0
# while m <= n:
#     sum = sum + m
#     count += 1
#     m = m + 1
# avg = int(sum / count)
# print("sum of all number is", sum, "and average is", avg)
# print(count)


# Date 04-10-2024


# sum of n digit number

# num = int(input("Enter your number: "))
# sum = 0
# while num != 0:
#     r = num % 10
#     num = int(num / 10)
#     sum += r
# print(sum)

# find revers of n digit number
# num = int(input("Enter your number: "))
# rev = 0
# while num != 0:
#     r = num % 10
#     num = int(num / 10)
#     rev = rev * 10 + r
# print("Revers of number is: ", rev)

# find a number is palindrome or not
# num = int(input("Enter your number: "))
# pen = num
# rev = 0
# while num != 0:
#     r = num % 10
#     num = int(num / 10)
#     rev = rev * 10 + r
# print("Revers of number is: ", rev)
# if pen == rev:
#     print("Number is palindrome")
# else:
#     print("Number id not palindrome")

#-----------------------------------------------------

# finding number is armstrong number or not
# num = int(input("Enter your number: "))
# arm = 0
# save = num
# while num!= 0:
#     r = num % 10
#     num = int(num / 10)
#     arm = arm + r * r * r
# if arm == save:
#     print("armstrong, yes")
# else:
#     print("armstrong, no")

#-----------------------------------------------------

# num = int(input("Enter your number: "))
# arm = 0
# save = num
# l = len(str(num))
# while num!= 0:
#     r = num % 10
#     num = int(num / 10)
#     arm = arm + pow(r, l)
# if arm == save:
#     print("armstrong, yes")
# else:
#     print("armstrong, no")

#-----------------------------------------------------

# num = int(input("Enter your number: "))
# arm = 0
# save = num
# num1=num
# count=0
# while num1!= 0:
#     r = num1 % 10
#     num1 = int(num1 / 10)
#     count=count+1
# while num!= 0:
#     r = num % 10
#     num = int(num / 10)
#     arm = arm + pow(r, count)
# if arm == save:
#     print("armstrong, yes")
# else:
#     print("armstrong, no")

#=======================================================================================

# Date 05/10/2024

# print all palindrome number upto n
# n = int(input("Enter the value of n: "))
# i = 1
# while i <= n:
#     num = i
#     save = num
#     rev = 0
#     while num != 0:
#         r = num % 10
#         num = int(num / 10)
#         rev = rev * 10 + r
#     if rev == save:
#         print(rev)
#     i += 1


#---------------------------------------------
# print all armstrong number upto n

#------------------------------------------------------

# n = int(input("Enter your number: "))
# i = 1
# while i <= n:
#     num = i
#     save = num # secure the temp 3
#     arm = 0
#     l = len(str(num))
#     while num!= 0:
#         r = num % 10
#         num = int(num / 10)
#         arm = arm + pow(r, l)
#     if arm == save:
#         print(save)
#     i += 1


#=================================================================================================
# for loop


# range
#-----------------------------
# for i in range (1, 11):
#     print(i)


#-----------------------------
# for i in range (20, 0, -1):
#     print(i, end=" ")

#-----------------------------
# odd number
# for i in range (1, 20, 2):
#     print(i)

#-----------------------------
#even number
# for i in range (2, 21, 2):
#     print(i)

#-----------------------------
#sum of 1 to n
# num = int(input("Enter number: "))
# sum = 0
# for i in range (1, num):
#     sum = sum + i
# print(sum)

#-----------------------------
# sum of n odd values
# num = int(input("Enter number: "))
# sum = 0
# for i in range (1, num+1):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)

#-----------------------------
# square of n number
# num = int(input("Enter N.: "))
# for i in range (1, num + 1):
#     res = i * i
#     print(res, end="\t")

#-----------------------------
# program to find factorial of a given number
# num = int(input("Enter number: "))
# fact = 1
# for i in range (1, num + 1):
#     fact = fact * i
# print(fact)


#-----------------------------
# pattern *****
# for i in range (1, 6):
#         print("*", end="")



#*****
#*****
#*****
#*****
#*****
# for i in range (1, 6):
#     for j in range (1, 6):
#         print("*", end=" ")
#     print()

#------------------------------------
#aaaaaaa
#bbbbbb
#ccccccc
#dddd
#eeeeeeeee

# for i in range (1, 6):
#     for j in range (1, 6):
#         if i == 1:
#             print("A", end="")
#         elif i == 2:
#             print("B", end="")
#         elif i == 3:
#             print("C", end="")
#         elif i == 4:
#             print("D", end="")
#         elif i == 5:
#             print("E", end="")
#     print()

#-------------------
#ABCDEf
#ABCDEf
#ABCDEf
#ABCDEf
#ABCDEf

# for i in range (1, 6):
#     for J in range (1, 6):
#         if J == 1:
#             print("A", end="")
#         elif J == 2:
#             print("B", end="")
#         elif J == 3:
#             print("C", end="")
#         elif J == 4:
#             print("D", end="")
#         elif J == 5:
#             print("E", end="")
#     print()


#-----------------------------------------
#******
#******
#**#***
#******
#******

# for i in range (1, 6):
#     for j in range (1, 6):
#         if i == 3 and j == 3:
#             print("#", end="")
#         else:
#             print("*", end="")
#     print()


#-------------------------------
#  (* # * # *)
#  (* # * # *)
#  (* # * # *)
#  (* # * # *)
#  (* # * # *)

# 1st 
# for i in range (1, 6):
#     for J in range (1, 6):
#         if J == 1:
#             print("*", end=" ")
#         elif J == 2:
#             print("#", end=" ")
#         elif J == 3:
#             print("*", end=" ")
#         elif J == 4:
#             print("#", end=" ")
#         elif J == 5:
#             print("*", end=" ")
#     print()


#--------------------------------
#2nd 
# for i in range (1, 6):
#     for j in range (1, 6):
#         if j % 2 == 0:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()



#--------------------------------------

# for i in range (1, 6):
#     for j in range (1, i+1):
#         print(j, end="")
#     print()

# 54321
# 5432
# 543
# 54
# 5
# for i in range (1, 6):
#     for j in range (5, i-1, -1):
#         print(j, end="")
#     print()

# 5
# 54
# 543
# 5432
# 54321
# for i in range (1, 6):
#     for j in range (5, 5-i, -1): # har step me se ak remove hog
#         print(j, end="")
#     print()


#===============================================================

# char  pattern
#ABCDE
#ABCDE
#ABCDE
#ABCDE

# for x in range(5):
#     for y in range(65,70):
#         print(chr(y), end=" ")
#     print()

# #2nd
# for x in 'ABCDE':
#     for y in 'ABCDE':
#         print(y, end=" ")
#     print()




#A
#AB
#ABC
#ABCD
#ABCDE
# for x in range (65,70):
#     for y in range (65,x+1):
#         print(chr(y), end=" ")
#     print()


#ABCDE
#ABCD
#ABC
#AB
#A
# for  x in range (65,70):
#     for y in range (65,135-x):
#         print(chr(y), end=" ")
#     print()

#2nd way
# for x in range(5,0,-1):
#     for y in range(0,x):
#         print(chr(y+65), end=" ")
#     print()

#EDCBA
#EDCB
#EDC
#ED
#E

# for x in range(0,5):
#     for y in range(4,x-1,-1):
#         print(chr(y+65), end=" ")
#     print()


#E
#ED
#EDC
#EDCB
#EDCBA

# for x in range (65, 70):
#     for y in range (69, 133-x, -1):
#         print(chr(y), end=" ")
#     print()

#    *
#   **
#  ***
# ****
#*****

# for i in range (1, 6):
#     for j in range (5, i, -1):
#         print(" ", end="")
#     for k in range (1, i+1):
#         print("*", end="")
#     print()


#    1
#   12
#  123
# 1234
#12345

# for i in range (1, 6):
#     for j in range (5, i, -1):
#         print(" ", end="")
#     for k in range (1, i+1):
#         print(k, end="")
#     print()


#    5
#   54
#  543
# 5432
#54321

# for i in range (1, 6):
#     for j in range (5, i, -1):
#         print(" ", end="")
#     for k in range (5, 5-i, -1):
#         print(k, end="")
#     print()


#*****
# ****
#  ***
#   **
#    *

# for i in range (1, 6):
#     for j in range (1, i):
#         print(" ", end="")
#     for k in range (5, i-1, -1):
#         print("*", end="")
#     print()

#12345
# 1234
#  123
#   12
#    1

# for i in range (1, 6):
#     for j in range (1, i):
#         print(" ", end="")
#     for k in range (1, 7-i):
#         print(k, end="")
#     print()



# 5
#  54
#   543
#    5432
#     54321

# for i in range (1, 6):
#     for j in range (1, i):
#         print(" ", end="")
#     for k in range (5, 5-i, -1):
#         print(k, end="")
#     print()


#     54321
#    5432
#   543
#  54
# 5

# for i in range (1, 6):
#     for j in range (5, i, -1):
#         print(" ", end="")
#     for k in range (5, i-1, -1):
#         print(k, end="")
#     print()


#     12345
#    1234
#   123
#  12
# 1

# for i in range (1, 6):
#     for j in range (5, i, -1):
#         print(" ", end="")
#     for k in range (1,7-i):
#         print(k, end="")
#     print()


#     E
#    ED
#   EDC
#  EDCB
# EDCBA

# for x in range (65, 70):
# #     for i in range (5,x-64, -1):  #5 start, x-64 if x is 65 then 65-64=1 means start is 5 and end is after 1 which is zero
#     for y in range (69,x,-1):
#         print(" ", end="")
#     for z in range (69, 133-x, -1):
#         print(chr(z), end="")
#     print()




#     12345
#    1234
#   123
#  12
# 1

# for x in range (1, 6):
#     for y in range (5, x, -1):
#         print(" ", end="")
#     for z in range (65,71-x):
#         print(chr(z), end="")
#     print()


# triangle * print
#     *
#    ***
#   *****
#  *******
# *********

# for x in range (1,6):
#     for y in range (5, x, -1):
#         print(" ", end="")
#     for z in range (1, 2*x):
#         print("*", end="")
#     print()

# *********
#  *******
#   *****
#    ***
#     *

# for x in range (1,6):
#     for y in range (1, x):
#         print(" ", end="")
#     for z in range (9, 2*x-2,-1):
#         print("*", end="")
#     print()



#     1
#    123
#   12345
#  1234567
# 123456789

# for x in range (1,6):
#     for y in range (5, x, -1):
#         print(" ", end="")
#     for z in range (1, 2*x):
#         print(z, end="")
#     print()


#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# for x in range (1,6):
#     for y in range (5, x, -1):
#         print(" ",end="")
#     for z in range (1, x+1):
#         print(z,end=" ")
#     print()


# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# for x in range (1,6):
#     for y in range (1, x):
#         print(" ",end="")
#     for z in range (1, 7-x):
#         print(z,end=" ")
#     print()



#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# for x in range (1,6):
#     for y in range (5, x, -1):
#         print(" ", end="")
#     for z in range (1, x+1):
#         print("*", end=" ")
#     print()
# for x in range (1,5):
#     for y in range (1, x+1):
#         print(" ", end="")
#     for z in range (1, 6-x):
#         print("*", end=" ")
#     print()



#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# for x in range (1,6):
#     for y in range (5, x, -1):
#         print(" ", end="")
#     for z in range (1, x+1):
#         print(z, end=" ")
#     print()
# for x in range (1,5):
#     for y in range (1, x+1):
#         print(" ", end="")
#     for z in range (1, 6-x):
#         print(z, end=" ")
#     print()




# 1 2 3 4 5 4 3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3       3 2 1
# 1 2           2 1
# 1               1
for i in range(1,6):
    for j in range(1,7-i):
        print(j, end=" ")
    for k in range(1,2*i-2):
        print(" ", end=" ")
    for l in range(6-i,0,-1):
        if l==5:
            continue
        else:
            print(l, end=" ")
    print()



# n=5
# a=n
# b=n
# for i in range(1,n+1):
#     for y in range(1,n*2+1):
#         if y <= a:
#             print(str(y)+" ",end="")
#         elif y >= b:
#             print(str(n*2-y-1)+" ",end="")
#         else:
#             print(" ", end="")
#     print()
#     a -=1
#     b +=1


# Jump Statement

# ...........BREAK.............

# for i in range(1, 50):
#     if i == 26:
#         break
#     print(i, end="  ") #output 1 to 25

# ................Example-2 Prime Number
# num = int(input("Enter your num: "))
# flag = 0
# for i in range(1, num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 0:
#     print("Prime Number")
# else:
#     print("Not a prime number")


# .................Continue
# ................Example-3

# i = 10
# while True:
#     for i in range (i,0,-1):
#         print(i, end=" ")
#     if i == 0:
#         break
#     i -= 1


# wap to print the number from 10 to 1
# wap to print the odd 1 to 20
# wap to print the even 1 to 20
# wap to print the natural no. 1 to N
# factorial value
# reverse of any digit
# sum of any n digit number
# print the table of a given number
