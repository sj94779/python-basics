f = open("demofile.txt", "r")



# for different location , like this 
# f = open("D:\\myfiles\welcome.txt", "r")


# thw whole text of the file

# print(f.read())
# or
# for x in f:
#   print(x)

# 5 chars only
# print(f.read(5))


# one line only
# print(f.readline())


# to close file 
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

f.close()


# the "w" method will overwrite the entire file.

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())


# create a new empty file
# f = open("myfile.txt", "x")


# delete existing file
# import os
# os.remove("myfile.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

