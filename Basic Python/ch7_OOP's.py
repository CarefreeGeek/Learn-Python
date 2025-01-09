# class Z:
#     def short(self):
#         count = int(input("Enter number of members: "))
#         li = []
#         while count != 0:
#             m = input("Enter your member: ")
#             li.append(m)
#             count -= 1
#         print("Members list is-",li)

# ob = Z()
# ob.short()
# .....................................................................................
# .....................................................................................
# --------SELF------------
# class A:
#     a=89
#     def dis(self,a):
#         print(a)
#         print(self.a)
# ob=A()
# ob.dis(67)
# print(ob.a)



# ------------------------------------------------------

# class A:
#     def counting(self):
#         count= 0
#         string = str.lower(input("Enter string: "))
#         vowel =str("aeiou")
#         for x in string:
#             for y in vowel:
#                 if x == y:
#                     count += 1
#         print(count)

# ob= A()
# ob.counting()



# .....................................................................................
# .....................................................................................
# ..................with argument
# class A:
#     def getdata(self,a,b):
#         self.x=a
#         self.y=b
#     def calsum(self):
#         sum=self.x+self.y
#         print(sum)       
# ob=A()
# ob.getdata(eval(input("enter the data")),eval(input("entre the data")))
# ob.calsum()

# class A:
#     sum = 0
#     def getdata(self, num1, num2,num3):
#         self.x= num1
#         self.y= num2
#         self.z= num3
#     def calsum(self):
#         self.sum=self.x+self.y+self.z
#     def average(self,):
#         avg = int(self.sum / 3)
#         print(avg)
# p = eval(input("enter the data"))
# q = eval(input("enter the data"))
# r = eval(input("enter the data"))
# ob=A()
# ob.getdata(p,q,r)
# ob.calsum()
# ob.average()



# class A():
#     def getnum(self, num):
#         for x in range(num):
#             for y in range(num):
#                 print(x+1, end=" ")
#             print()
# # a = int(input("Enter range: "))
# ob=A()
# ob.getnum(5)



# sum of n numbers
# class A:
#     def calsum(self, num):
#         self.sum = 0
#         while num != 0:
#             self.sum += num
#             num -= 1
#         print(self.sum)
# num = int(input("Enter n: "))
# ob=A()
# ob.calsum(num)



# ....................Constructure............................
# ....................Constructure............................
# ....................Constructure............................

# class A:
#     def __init__(self):
#         print("i am a coinstructor")

# ob=A()


# class A:
#     def __init__(self, string1):
#         self.s= string1
#         return print(f"Your original string is: {self.s}")
#     def exch(self):
#         n = len(self.s)
#         a= self.s[0]
#         z= self.s[-1]
#         res = z + self.s[1:n-1] +a
#         return print(f"Exchanged string is: {res}
# ")

# string1 = str(input("Enter string: "))
# ob = A(string1)
# ob.exch()



# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1




# ...................Inheritance........................
# ...................Inheritance........................
# ...................Inheritance........................



# class A:
#     username = "Abhinav"
#     password = "Abhi@123"
#     def __init__(self):
#         self.username_input = str(input("Enter Username: "))
#         self.password_input = str(input("Enter password: "))

# class B(A):
#     def Check(self):
#         if self.username_input == self.username and self.password_input == self.password:
#             print("Login Successfull")
#         else:
#             print("Invalid Username or Password")

# obj = B()
# obj.Check()



# class A:
#     def __init__(self):
#         self.a = int(input("ENter num1: "))
#         self.b = int(input("ENter num2: "))

# class B(A):
#     def calsum(self):
#         self.sum = self.a+self.b
#         print("sum is:")
#         return self.sum

# class C(B):
#     def average(self):
#         avg = (self.sum / 2)
#         print("average is:")
#         return avg

# ob = C()
# ans=ob.calsum()
# print(ans)
# res=ob.average()
# print(res)






# class A:
#     def dis(self):
#         self.a = int(input("ENter num1: "))
#         self.b = int(input("ENter num2: "))
#         self.c = int(input("ENter num3: "))

# class B(A):
#     def calsum(self):
#         self.sum = self.a+self.b+self.c
#         print("sum is: ",self.sum)

# class C(A):
#     def great(self):
#         if self.a > self.b and self.a > self.c:
#             print(f"{self.a} is greater")
#         elif self.b > self.a and self.b > self.c:
#             print(f"{self.b} is greater")
#         else:
#             print(f"{self.c} is greater")
    
# ob1= B()
# ob2= C()
# ob1.dis()
# ob1.calsum()
# ob2.dis()
# ob2.great()





# class A:
#     def getdata(self):
#         self.a = int(input("Enter value: "))
#         return self.a

# class B(A):
#     def calsum(self):
#         sum = 0
#         self.getdata()
#         for num in range(5):
#             sum = sum + self.a
#             print(sum)

# ob = B()
# ob.calsum()





# class A:
#     def dis(self,a,b):
#         self.a=a
#         self.b=b
#     def disa(self):
#         print(self.a)
#         print(self.b)
# ob=A()
# ob.dis(12,56)
# ob.disa()



# ..................Polymorphism........................
# ..................Polymorphism........................
# ..................Polymorphism........................

