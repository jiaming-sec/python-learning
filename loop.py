# Python has two primitive loop
# while loops
# for loops

# while loop
# with "while" loop, we can execute a set of statements as long as a condition is true
# print i as long as i is less than 6
i = 1
while i < 6:
  print("i")
  i += 1

# the "break" statement
# with "break" statement we can stop the loop even if the while condition is true:
i = 1 
while i < 6:
  print(i)
  f i ==3:
    break
  i +=1 

# the "continue" statement
# with "continue" statement we can stop the current iteration, and continue with the next

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6

# with "else" statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else: 
  print("i is no longer less than 6")


# "for" loop is used to iterate over a sequence (list, tuple, dictionary, set, string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# "for" loop does not require an indexing variable to set beforehand

# loop through a String
# Even strings are iterable objects, they contain a sequence of characters
for x in "banana":
  print(x)

# "break statement
# break statement can stop the loop before it has looped through all items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# "continue" statement
# continue statement can stop current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The "range()" 
# To loop through a set of code a specified number of items

# "range()" function return a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at specified number
for x in range(6):
  print(x)

# range(6) is not the values of 0 to 6, but the values 0 to 5
# range(2,6), which means vales from 2 to 6 (not including 6)















