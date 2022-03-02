# remember that in python, variables are just names pointing to the value. in the following example, both x and y points to same value, means when x changes yalso changes.

x = [1, 2, 3]
y = x
x.append(20)
print(x)
print(y)
