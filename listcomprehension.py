# List comprehension provides a concsie way to create lists. Each list comprehensio consists of an expression followed by a clause. then zero or more for it clause. the result will be the list resulting from evaluatiing the expression in the context of the for and if clauses which follow it.

# for example if we want to make a list out of the square values of another list.

a = [1, 2, 3]
z = [x ** 2 for x in a]
print (z)
Z = [x + 1 for x in [x ** 2 for x in a]]
print (Z)

# Above in the second case we used two list comprehension in a same line.


