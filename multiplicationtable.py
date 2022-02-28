# In this example we are going to print the multiplication table up to 10.

i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print ("%4d" % (i * n), end=' ')
        n += 1
        print()
        i += 1
        print("-" * 50)
