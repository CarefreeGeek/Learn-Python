#date 26-09-2024
# taking input

# a = 57
# b = 34
# add = a+b
# sub = a-b
# mul = a*b
# div = a/b
# print("a= 57 \n b= 34")
# print("add. of a is ", add)
# print("sub. of a is ", sub)
# print("mul. of a is ", mul)
# print("div. of a is ", div)



#-------------------------------------

# a = "Hello"
# b = 6
# print(id(a))
# print(id(b))

#taking user input using input() method
# var =______input()  can use input data type or it take and use value as it is.

# var = input()
# print(var)

# #*****Examples1*********

# side = int(input("Enter your side value: "))
# result = side * 2
# print("area square of side",side, "is ", result)

#******Example2**********

# width = int(input("Enter your width value: "))
# height = int(input("Enter your height value: "))
# result = height * width
# print("area of rectangle width",width, "and height ", height, "is:", result)


#********Example3*********

# width = int(input("Enter your width value: "))
# height = int(input("Enter your height value: "))
# length = int(input("Enter your length value: "))
# result = height * width * length
# print("volume cube of width,",width, " height,", height, "and length", length, "is:", result)

#**********Example4*********


# l = int(input("Enter your side value: "))
# w = int(input("Enter your side value: "))
# result = 2 * (l + w)
# print("parameter of rectangle is: ", result)



#**********Example5*********


# b = int(input("Enter your braces value: "))
# result = 4 * b
# print("parameter of square is: ", result)


#**********Example6***********


# day = int(input("Enter your days value: "))
# result = day * 24
# print(day, "days in hours is: ", result)


#**********Example7***********

# year = int(input("Enter your year value: "))
# result = year * 12
# print(day, "year in month is: ", result)




#--------------------HOME WORK----------------------

#1. average calculator.................

# a = int(input("Enter the first Number: "))
# b = int(input("Enter the second Number: "))
# c = int(input("Enter the third Number: "))
# avg = (a + b + c) / 3
# print("Average of three numbers is: ", avg)

# #2 temperature convertor
# celsius = int(input("Enter the temperature in celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in fahrenheit is: ", fahrenheit)



#3 discount calculator
# price = int(input("Enter the price of the product: "))
# discount = int(input("Enter the discount percentage: "))
# discounted_price = price - (price * discount / 100)
# print("Discounted price is: ", discounted_price)



# 4 factorial of a number
# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
#     print("Factorial of the number is: ", factorial)


# 5 square root of a number
# import math
# num = int(input("Enter the number: "))
# square_root = math.sqrt(num)
# print("Square root of the number is: ", square_root)


#6. percentage calculator
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# percentage = (num1 / num2) * 100
# print("Percentage is: ", percentage)

#.............................................................................
# wap to convert the km into meter
# km = int(input("Enter the distance in km: "))
# meter = km * 1000
# print("Distance in meter is: ", meter)


# wap to convert the meter into cm
# meter = int(input("Enter the distance in meter: "))
# cm = meter * 100
# print("Distance in cm is: ", cm)



# wap to convert the minutes into seconds
# minute = int(input("Enter the time in minute: "))
# second = minute * 60
# print("Time in second is: ", second)


# wap to convert the month into days
# month = int(input("Enter the month: "))
# days = month * 30
# print("Days in month is: ", days)




# wap to convert the month into weeks
# month = int(input("Enter the month: "))
# weeks = month * 4
# print("Weeks in month is: ", weeks)




#===========================================================================================


#date 27-09-2024
# playing with input and maths

# #************Example1*************
# swap two number using third variable

# a = 15
# b= 20
# print("before a =",a)
# print("before b =",b)

# temp = a
# a = b
# b = temp
# print("after a =",a)
# print("after b =",b)
# by user input------------------------------
# a = int(input("Enter first value a: "))
# b = int(input("Enter first value b: "))
# temp = a
# a = b
# b = temp
# print("after a =",a)
# print("after b =",b)

#********Example2******************
# area of triangle
# base = int(input("Enter base of triangle: "))
# height = int(input("Enter height of triangle: "))
# area = 0.5 * base * height
# print("area of triangle is ",area)

# **********Example3*********************

# equation of kinetic energy
# print("To get kinetic energy value")
# m = int(input("Enter mass: "))
# v = int(input("Enter velocity: "))
# K = 0.5 * m * v * v
# print("Kinetic energy is ",K)

# **********Example4*********************
# print number into diff slices
# num = int(input("Enter 5 digit value to slice: ")) #12345
# value1 =int(num % 10) # 12345 % 10 = 5(value1)
# num = num / 10
# value2 = int(num % 10)
# num = num / 10
# value3 = int(num % 10)
# num = num / 10
# value4 = int(num % 10)
# num = num / 10
# value5 = int(num % 10)
# result = value1 + value2 + value3 + value4 + value5
# print("Sum of value number is: ", result)



# meter in km and meter
# km = int(input("Enter meter value: "))
# c = int(km / 1000)
# b = km % 1000
# print(c,"Kilometer and" ,b, "meter")



# # revers the 5 digit number
# num = int(input("Enter number to reverse"))
# value1 = int(num % 10)
# value1 = value1 * 10000
# num = num / 10






# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate: "))
# time = float(input("Enter the time period in years: "))

# simple_interest = (principal * rate * time) / 100
# total_amount = principal + simple_interest

# print("Simple Interest: ", simple_interest)
# print("Total Amount: ", total_amount)