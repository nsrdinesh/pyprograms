
"""
Explain the Mutable and Immumtable behaviours

"""

# Immutable
x = 10
print(id(x))

x = 20
print(id(x))

# Mutable
y = [1, 2, 3]
print(id(y))
y.append(4)
print(id(y))


# Numbers

x = 0x10 # hex
x = 0b10 #binary
print(x)

print (bin(x))
print (hex(x))

x = 1 + 2j  #complex numbers - needed for the maths computing.
print(x)


