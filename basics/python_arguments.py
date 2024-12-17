def average(*numbers):
    print (type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print("Average is: " , sum /len(numbers))

average(4,6,9,4)    

# single * argument will be considered as tuple
# double ** argument will be considered as dict

#set and dict are unordered one .


def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(lname = "Bachhan", mname = "Amitabh" , fname = "Abhishek" )    