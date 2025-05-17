# Python does not have built-in support for Arrays, Python "lists" can be used instead
# To work with arrays in Python, have to import a library, like the "Numpy" library

my_array = [7,12,9,4,11]
print(my_array[0])

# find the lowest value in an Array
# 1. create a variable 'minVal' and set it equal to the first value of the array
# 2. go through every element in the array
# 3. if the current element has a lower value than minVal, update minVal to this value
# 4. after looking at all the elements in the array, the minVal variable now contains the lowest value

Variable 'minVal' = array[0]
For each element in the array
  if current element < minVal
    minVal = current element

arr = [7, 12, 9, 4, 11]
minVal = arr[0] # step 1

for i in arr: # step 2
  if i < minVal: # step 3
    minVal = i 
print('lowest value: ', minVal) # step 4

# Selection Sort (Solution: Swap Values!)
# Instead of all the shifting, swap the lowest value (5) with the first value (64) like below.
# Move the lowest value to the front of the unsorted part of the array
