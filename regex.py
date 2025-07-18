# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
import re

# search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("The.*Spain$", txt)

----------------------------------------------------
#RegEx Functions
# re modue offeres a set of functions that allows us to search a string for a match:

# findall -- Returns a list containing all matches
# search -- Returns a Match object if there is a match anywhere in the string
# split -- Returns a list where the string has been split at each match
# sub -- Replaces one or many matches with a string

----------------------------------------------------
# Metacharacters are characters with a special meaning:
# []	A set of characters	"[a-m]"
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)


# \	Signals a special sequence (can also be used to escape special characters)	"\d"
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)


# .	Any character (except newline character)	"he..o"
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)


# 
