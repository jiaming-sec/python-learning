# python conditions and if statements
a == b
a != b
a < b
a <= b
a > b
a >= b

# "if statement" is written by using "if" keyword
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

# Elif
# "elif": if the previous conditions were not true, then try this condition
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
# 
