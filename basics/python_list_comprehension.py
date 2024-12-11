fruits = ["apple" , "banana" , "orange", "grape", "lichi", "chiku"]
newList = []
for x in fruits :
    if "a" in x :
     newList.append(x)
print(newList)   

#m2
#newList = [x for x in fruits if "a" in x]
#print(newList);

newList = [x for x in fruits if x != "apple"]
print(newList)

newList = [x.upper() for x in fruits]
print(newList)

newList = ["Hello" for x in fruits]
print(newList)


#Return the item if it is not banana, if it is banana return orange.
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)

list1 = ["a" , "b" , "c"]
list2 = [1 , 2 , 3]
list3 = list1 +list2
print(list3)

for x in list2 :
   list1.append(x)
   print(list1)


list1.extend(list3)
print(list1)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


thisTuple = ("Apple" , "Orange" , "Banana")
i = 0
while i < len(thisTuple) :
   print(thisTuple[i])
   i = i + 1


tuple1 = ("a" , "b" , "c")
tuple2 = ("1" , "2" , "3")
tuple3 = tuple1 + tuple2
print(tuple3) 

myTuple = tuple1 * 2
print(myTuple)


# command to run
# cd basics
# python3 python_list_comprehension.py