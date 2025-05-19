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

# The "self" parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
