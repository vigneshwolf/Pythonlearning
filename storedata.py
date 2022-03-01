#We can store anything in the list, so first we are going to add another list b in a; then we will learn how to add the values of b into a.

a = [23, 45, 1, -3434, 43624356, 234]
b = [45, 56, 90]
a.append(b)
print(a)
a[-1]
print(a[-1])
a.extend(b)
print(a)
a[-1]
print(a[-1])
#Above we can see we have used the a.extend() method to extend the list. to sort any list we have sort()method.the sort method will only work if the element in the list are comparable. we will remove the list b from the list and then sort.
a.remove(b)
print(a)
a.sort()
print(a)
#you can also delete an element at any particular position of the list using the del keyword.

del a[-1]
print(a)
