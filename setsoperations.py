# And some example of set operations.

a = set('abcdefghijklmnop')
b = set('qrstuvwxyz')

print (a)                     # unique letters in a 
print (a - b)                 # letters in a but not in b
print (a | b)                 # letter in either a or b
print (a & b)                 # letter in both a and b
print (a ^ b)                 # letter in a or b but not both
