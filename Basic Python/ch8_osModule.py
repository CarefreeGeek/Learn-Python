import os 

# =================================================
# printing OS name version

# print(os.name)


# =================================================
# printing current working directory

# cwd = os.getcwd() 
# print("Current working directory:", cwd)



# =================================================
# get back to the previous dir

# def current_path(): 
#     print("Current working directory before") 
#     print(os.getcwd()) 
#     print() 
# current_path() 
# os.chdir('../') 
# current_path()


# =================================================
# showing all files in dir

# path = "/pyt"
# dir_list = os.listdir(path) 
# print("Files and directories in '", path, "' :") 
# print(dir_list)

# =================================================
# create the directory

# directory = "GFG"
# parent_dir = "E:/pyt/"
# path = os.path.join(parent_dir, directory) # or ('E:/pyt/', 'GFG')
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# =================================================
# del the specifuc file

# file = 'h3.py'
# location = "E:/pyt/"
# path = os.path.join(location, file)
# if path == True:
#     os.remove(path)
#     print("File deleted")
# else:
#     print("something wrong!")

# =================================================
# remove the directory

# directory = "temp"
# parent = "E:/pyt/"
# path = os.path.join(parent, directory) 
# os.rmdir(path)

# =================================================
# file readind mode error

# try:
#     filename = 'GFG.txt'
#     f = open(filename, 'r')
#     text = f.read()
#     print(text)
#     f.close()
# except IOError:
#   print('Problem reading: ' + filename)



# =================================================
# file writing mode error

# try:
#     filename = 'GFG.txt'
#     f = open(filename, 'w')
#     f.write('Hello, world!')
#     f.close()
# except IOError:
#     print('Problem writing: ' + filename)



# =================================================
# rename the file

# fd = "GFG.txt"
# os.rename(fd,'New.txt')



# =================================================
#importing os module.

# os.remove("file_name.txt") #removing the file.


# =================================================
#importing os module

# size = os.path.getsize("filename")
# print("Size of the file is", size," bytes.")