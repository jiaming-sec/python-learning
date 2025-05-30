mylist = ["apple", "banana", "cherry"]

#list are one of 4 built-in data types in Python (Tuple, set, Dictionary")

print(mylist)
#list items are ordered, changeable, and allow duplicate values
# first index [0]

# list length
print(len(mylist))

#lists are defined as objects with data type 'list
<class 'list'>

# list() constructor
thislist = list(("apple", "banana"))

# 4 collection data types in Python
# List - ordered, changeable. Allows duplicate
# Tuple - ordered, unchangeable. Allow duplicate
# Set - unordered, unchangeable, unindexed, no duplicate
# Dictionary - ordered, changeable, no duplicate

# The first item has index 0
# Negative indexing -1 refers to the last item, -2 refers to the second last item.

# Check if item exists
# To determine if a specified item is present in a list use the in keyword

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# insert items
# insert a new list item without replacing any existing values, use insert() method
thislist.insert(2, "watermelon")

# append item
# to add an item to the end of the list, use append() method
thislist.append("orange")

# Extend list
# to append elements from another list to the current list, use extend() method
tropical = ["mango","pineapple", "papaya"]
thislist.extend(tropical)

# extend() method does not have to append lists, can add any iterable object (tuples, sets, dictionaries)

# remove specified item
# the remove() method removes the specified item
thislist.remove("banana")

# if there are more than one item (duplicate) with the specified value, the remove() method removes the first occurrence 

# remove specified index
# pop() method removes the specified index
thislist.pop(1)

# if you do not specify the index, the pop() method removes the last item.
thislist.pop()

# the "del" keyword also removed the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]

# "del" can also delete the list completely
del thislist

# clear the list
# clear() method empties the list
thislist.clear()

# loop through a list
# loop throught the list items by using "for" loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)










































