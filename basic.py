
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
