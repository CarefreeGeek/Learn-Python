import array as arr
from array import *

# a=arr.array(data type,value list)           #when you import using arr alias
# OR
# a=array(data type,value list)               #when you import using *


# after importing array
# we can use array() function to create an array object
# array() function takes an iterable as an argument and returns an array object
# array() function can take a typecode as an argument to specify the type of elements in the
# array object
# typecode is a single character that specifies the type of elements in the array object
# typecode can be 'b' for signed integer, 'B' for unsigned integer, '
# 'u' for Unicode character, 'h' for signed short integer, 'H' for
# unsigned short integer, 'i' for signed integer, 'I' for unsigned integer, '
# 'l' for signed long integer, 'L' for unsigned long integer, 'q'
# for signed long long integer, 'Q' for unsigned long long integer, 'f' for
# float, 'd' for double, 'c' for character, 's' for string
# array() function returns an array object with the specified typecode and elements
# array() function can also take a list as an argument to create an array object with the
# specified elements and typecode

# Type code	Python Data Type	Byte size
#     i,I	    int             	2
#     h,H      	int             	2
#     l,L      	int             	4
#     q,Q    	long integer	    8
#     f       	float           	4
#     d       	float           	8
#     B       	unsigned byte	    1
#     b       	signed byte	        1
#     s       	string (bytes)	    2
#     S       	string (unicode)	2
#     u	        unicode character	2
#     U       	unicode character	4
#     p       	python object   	8


# Creating arrays examples 

# a=array('i',[1,2,3,4,5])  #int array (I or i)
# a=array('f',[1.2,2.3,3.4,4.4]) #float array (F or f)
# a=array('c',['a','b','c','d'])  #character array (C or c)
# a=array('u',['apple','banana','cherry'])  #unicode array (U or u)
# a=array('b',[1,0,1,0,1])  #boolean array (B or b)
# a=array('l',[[1,2,3],[4,5,6]]) #2D array (L or l)
# a=arr.array('i',range(1,11)) #int array from 1 to
# a=array('i',range(1,11,2)) #int array from 1

# print(a)
#==========================================================
# Accessing array elements in Python :
# Array_name[index value]
# print(a[2])

# leangth of an array
# print(len(a))

# ==========================================================
# Adding/ Changing elements of an Array:

# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.append(3.4)
# print(a) #Adding an element at the end of the array

# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.extend([4.5,6.3,6.8])
# print(a) #Adding multiple elements at the end of the array

# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.insert(2,3.8)
# print(a) #Inserting an element at a specified index

# =========================================================
# Array Concatenation

# a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("Array c = ",c)

# ==========================================================
# Removing/ Deleting elements of an array:

# a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
# print(a.pop())
# print(a.pop(3))

# a=arr.array('d',[1.1 , 2.1 ,3.1])
# a.remove(1.1)
# print(a)

# ==========================================================
# Slicing an array :

# a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
# print(a[0:3])

# ==========================================================
# Looping through an array:

# a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
# print("All values")
# for x in a: 
# print(x)
# print("specific values")
# for x in a[1:3]: 
# print(x)


