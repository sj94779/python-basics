x = lambda a : a + 10
print(x(10))

x = lambda a , b : a * b
print(x(5,6))

def myFunc(n):
    return lambda a : a*n

myDoubler = myFunc(2)
myTripler = myFunc(3)

print(myDoubler(11))
print(myTripler(11))


# command to run
# cd basics
# python3 python_lambda_func.py

    