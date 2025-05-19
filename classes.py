# create a class
class MyClass:
  x = 5

# create object
p1 = MyClass()
print(p1.x)

# "_init_()" function
# all classes have a function called _init(), which is always executed when the class is being initiated
# use _init_() to ass values to object properties, or other operations that are necessary to do when the object is being created

class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age
  p1 = Person("John", 36

  print(p1.name)
  print(p1.age)

# Object methods
# Methods in objects are functions that belong to the object.             
# The "self" parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
