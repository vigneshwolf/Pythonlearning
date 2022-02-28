# In your print function call if you pass another argument called end and pass another argument called end and pass a space string. it will print in the same line with space delimiter. The default value for end is '\n'.

a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b
