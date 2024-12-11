a = 200
b = 33
if a > b :
    print("a is greater than b")
elif a == b :
    print("a is equal to b")
else :
    print("a is less than b")   

# shorthand

a = 2
b = 200
print("a") if a >b else print("b")  
print("a") if a > b else print("=") if (a == b) else print("b")  

a = 20
b = 48
c = 10
if a > b and c > a :
    print("Both conditions are true")

if a < b or b < c :
    print("At least one of the condition is true")   

if not a > b :
    print("a is not greater than b")

x = 30
if x > 10 :
    print("Above 10") 
    if x > 20 :
        print("and also above 20")
    else:
        print("but not above 20")           


# command to run
# cd basics
# python3 python_conditionals.py