fruits = ["Apple" , "Banana" , "Orange"]
for x in fruits:
    if x == "Orange" :
     break
    print(x)


for x in fruits:
   if x == "Banana" :
      continue
   print(x)    


adj = ["red" , "big" , "tasty"]

for x in adj:
   for y in fruits:
      print(x ,y)


i = 1
while (i <6):
   print(i)
   if i ==3:
     break

   i += 1

i=1
while (i<6):
   i +=1
   if i==3:
    continue 
   print(i)


# command to run
# cd basics
# python3 python_loops.py