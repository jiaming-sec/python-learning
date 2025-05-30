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
# "else": catches anything which isn't caught by the preceding condition.
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a ==b :
  print("a and b are equal")
else:
  print("a is greater than b")

# short hand if: if you have only one statement to execute, you can put it on the same line
if a > b: print("a is greater than b")

# short hand if...else: one for if, and one for else, put all on the same line
a = 2
b = 330
print("A") if a > b else print("b")

print("A") if a > b else print("=") if a == b else print("B")

# "and" is logical operator, use to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print()
if not a > b:
  print()

# "pass" statement
# "if" statment cannot be empty, if you have "if" statment with no content, put in the "pass" statement to avoid getting an error
a = 33
b = 200
if b > a:
  pass

# "match" statement is used to perform different actions based on different conditions
# Instead of writing many if...else statements, you can use "match" statement.

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Default Value
# use the underscore "_" as the last case value if you want a code block to execute when there are not other matches
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# Combine Values
# use pipe character "|" as an "or" operator in the case evaluation to check
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print(":Weekends")

# if statements as guards
# add "if" statements in case evaluation as an extra condition-check
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match") 























