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