# function is a block of code which only runs when it is called
# you can pass data -> parameters into function

# function is defined using "def" keyword
def my_function():
  print("Hello from a function")

# calling a function
# to call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()

# arguments


# Recursion
# Function recursion means defined function can call itself
def tri_recursion(k):
  if k > 0 :
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0

return result

print("Recursion example results:")
tri_recursion(6)
