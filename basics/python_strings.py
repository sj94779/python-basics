a = "Hello World"
print(len(a))

print(a[1])

#check if "llo" is present in the string
print("llo" in a)

if "llo" in a :
    print("yes it is there")

if "llo" not in a :
    print("No not present")    

for x in "banana":
    print(x)

print(a[2:5])    

print(a[:4])

print(a[2:])

print(a[-5:-2])

print(a.upper())

print(a.lower())


#removes before or after spaces not between
print(a.strip())

print(a.replace("H" , "J"))

print(a.split(","))

x = "demo1"
y = "demo2"
z = x + y
print(z)

w = x + " " + y
print(w)

# F-String
age = 22
txt = f"My age is {age}"
print(txt)

#upto two decimals
t = 49
txt = f"The price is {t:.2f}"
print(txt)


txt = f"The price is {2*9} dollers"
print(txt)

#incorrect
# txt = "We are the so-called "Vikings" from the north."

#correct
txt = "We are the so-called \"Vikings\" from the north."
   
# command to run
# cd basics
# python3 python_strings.py



letter = "Hey my name is {1} and I am from {0}"
country="India"
name="Harry"

print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollers!"
print(txt)

print(type(f"{2*30}"))


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

    
square(5)
print(square.__doc__)