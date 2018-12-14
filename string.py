name = "Dinesh Kumar Santhanaraman"

print(len(name))

print(name[0:2])
print("*" * len(name[0:2]))
print(name[0:-4])
print("*" * len(name[0:-4]))

print(name[0:])
print("*" * len(name[0:]))

# strings are mutable

print(id(name))
print(id(name[2]))


#double quotes in the middle of string

print (" Dinesh \" Kumar \" ")

message = """
Testing
Multiline
"""

print(message)

# Formated Strings 
# Any valid expression can be placed in the {} braces 

first = "Dinesh"
last = "Kumar"
full_name = f"{first}  {len(last)}"

print (full_name)


# Use ful string functions

test_string = "  Python Programming  "

print (test_string.upper())
print (test_string.lower())
print (test_string.title())

print (test_string.strip())

# string find characters

print( test_string.find("pro")) # -1 tells not found.

print(test_string.replace("P", "-"))

print ("Programming" in test_string)