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


























