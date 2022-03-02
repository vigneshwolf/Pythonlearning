# There are two other functions related to boolean value checking. any and all any tells us if any of the value in the list if true. all tells us if any of the value in the list are true or not.

numbers = [0, 1, 2, 3, 4, 5, 6]
a = any(numbers)
print (a)
b = all(numbers)
print (b)

# Here all returned False because we have 0 in the list.
