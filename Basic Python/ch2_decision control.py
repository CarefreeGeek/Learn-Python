# date 28-09-2024
# decision control statement
# if, if-else, else-if statement


# #***********Example1**********
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# if a > b:
#     print("first value is greater then second value")
# else:
#     print("second value is greater then first value")


#***********Example2**********

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are elidible for voting")
# else:
#     print("You are not elidible for voting")



#***********Example3**********
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# if a > b and a > c:
#     print("first value is greater")
# elif b > c and b > a:
#     print("second value is greater")
# elif c > a and c > b:
#     print("third value is greater")
# else:
#     print("all are equal")

#***********Example4**********
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even.")
# else:
#     print(num, "is odd.")

#***********Example5**********
# year = int(input("Enter a year.."))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, "is a leap year.")
# else:
#     print(year, "is not leap year.")


#***********Example6**********
# a = int(input("Enter first degree value: "))
# b = int(input("Enter second degree value: "))
# c = int(input("En*ter third degree value: "))
# if a + b + c == 180:
#     print("yes it is Triangle")
# else:
#     print("no it is not Triangle")

#***********Example7**********
# a = int(input("Enter first side value: "))
# b = int(input("Enter second side value: "))
# c = int(input("Enter third side value: "))
# if (a + b) > c or (a + c) > b or (b + c) > a:
#     print("yes it is Triangle")
# else:
#     print("no it is not Triangle")


#***********Example*8*********

# cubic volume
# a = int(input("Enter length of cube: "))
# volume = a ** 3
# print("volume of cube is: ", volume)

# # cubic surface area
# a = int(input("Enter length of cube: "))
# surface_area = 6 * (a ** 2)
# print("surface area of cube is: ", surface_area)


#==================================================================================


#date 29-09-2024

# nested if-else within else
#-------------------------------------------
# h = int(input("Enter height of rectangle: "))
# w = int(input("Enter width: "))
# area = h * w
# Perimeter = 2 * (h + w)
# if area > Perimeter:
#     print("Area is greater than perimeter")
# else:
#     if area < Perimeter:
#         print("Perimeter is greater than area")
#     else:
#         print("Area and perimeter are equal")

#-----------------------------------------------


# radius = int(input("Enter height of circle "))
# area = 3.14 * radius * radius
# circumference = 2 * 3.14 * radius
# if area > circumference:
#     print("Area is greater than circumference")
# else:
#     if area < circumference:
#         print("circumference is greater than area")
#     else:
#         print("Area and circumference are equal")

#-----------------------------------------------

# comparison cuboid area and surface volume

# l = int(input("Enter first value: "))
# w = int(input("Enter second value: "))
# h = int(input("Enter third value: "))

# surface_area = 2 * (l * w + w * h + l * h)
# volume = l * w * h
# if volume > surface_area:
#     print("volume is greater than surface area")
# else:
#     if volume < surface_area:
#         print("surface area is greater than volume")
#     else:
#         print("volume and surface area are equal")



#date 30-09-2024

#-----------------------elif ladder----------------------------------------------

# **********Example1*********************
# checking number is negative, positive or zero

# num = int(input("Enter number"))
# if num < 0:
#     print("Number is negative")
# elif num == 0:
#     print("Number is zero")
# else:
#     print("Number is positive")

# **********Example2*********************
# comparison cuboid area and surface volume

# l = int(input("Enter first value: "))
# w = int(input("Enter second value: "))
# h = int(input("Enter third value: "))
# surface_area = 2 * (l * w + w * h + l * h)
# volume = l * w * h
# if volume > surface_area:
#     print("volume is greater than surface area")
# elif volume < surface_area:
#         print("surface area is greater than volume")
# else:
#         print("volume and surface area are equal")

# Date 01-10-2024
#short hand if-else


#---------------Example1-------------------
# grade program
# marks = int(input("Enter your marks in %: "))
# if marks <= 100 and marks >= 90:
#     print("Hurray! you achieved grade A")
# elif marks <= 89 and marks >= 80:
#     print("Great, you achieved grade B")
# elif marks <= 79 and marks >= 70:
#     print("Good,you achieved grade C")
# elif marks <= 69 and marks >= 60:
#     print("you achieved grade D")
# elif marks <= 59 and marks >= 0:
#     print("sadly you are failed")
# else:
#         print("Enter value from 0 to 100")

#======================================Short Hand if-else=====================================================

# negative or positive
# num = int(input("Enter num"))
# print("even") if num % 2 ==0 else print("odd")

# leap year
# year = int(input("Enter year"))
# print("leap year") if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else print("not leap year")

