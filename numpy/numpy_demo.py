import numpy as np

arr = np.array([1,2,3,4,5])  #list to ndarray

#or

arr = np.array((1,2,3,4,5))   # tuple to ndarray

print(arr)

print(type(arr))

# command to run: 
# cd numpy
# python3 numpy_demo.py

# dimension array for tensor/data science
arr = np.array([1,2,3,4] , ndmin = 5)

print(arr)

print("number of dimensions" , arr.ndim)

arr = np.array(("Hello" , "World"))

print(arr[0] + " " + arr[1])


# 3D array get element
arr = np.array([[[1,2,3] , [4,5,6] , [7,8,9] , [10,11,12]]])
# 0 means 1st dimension, 1 means 2nd row, 2 means 3rd element
print("element at arr[0,1,2] is" , arr[0,1,2])

# slicing

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[1:5])
print(arr[:4])
print(arr[4:])
print(arr[-3:-1])

# array type change

arr = np.array([1.1 , 2.4 , 4.2])
newarr = arr.astype(int)
print(newarr)
print(arr.dtype)
print(newarr.dtype)

arr = np.array([1,0,8])
newarr = arr.astype(bool)
print(newarr)
print(arr.dtype)
print(newarr.dtype)


# copy v/s view
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 48
print(arr)
print(x)

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 90
print(arr)
print(x)


#shape , reshape
#(dimension, no. of elements per dimension)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.shape)

x = arr.reshape(4,3)
print(x)

# 2 array with 3 array containing 2 items each
y = arr.reshape(2, 3,2)
print(y)


print(arr.reshape(2,6).base)
# copy base : None
# view base : original array

#flattening
# convert multidimension to flat 1D array
arr = np.array([[1,2,3], [4,5,6]])
newarr = arr.reshape(-1)
print(newarr)

for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)    

arr = np.array([[[1,2], [3,4], [5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)

# element with index / enumerated

arr = np.array([1,2,3])
for idx , x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1,2],[3,4]])
for idx , x in np.ndenumerate(arr):
    print(idx,x)    


# join / concatenate
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.vstack((arr1, arr2))
print("arr3 is " ,arr3)

arr4 = np.hstack((arr1,arr2))
print("arr4 is " ,arr4)

arr5 = np.stack((arr1, arr2) , axis = 1)
print("arr5 is " ,arr5)

arr6 = np.dstack((arr1, arr2))
print("arr6 is " ,arr6)

#split
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
x = np.array_split(arr, 3)
print(x)

# search
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr==4)
print(x)
#returns indexs

x = np.where(arr%2 == 0)
# returns even value indexs
print(x)

#searchsorted / where to insert to get sorted array ,, returns indexs
arr = np.array([6,7,8,9])
x = np.searchsorted(arr, 7)
print(x)

#sort
arr = np.array([[3,9,1],[0,7,1]])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

#filter array

arr = np.array([41,42,43,44])
x = [True,False, True ,False]

print("filtered array is " , arr[x])

filter_array = arr > 42
print(arr[filter_array])

filter_array = arr % 2 == 1
#odd only
print(arr[filter_array])





