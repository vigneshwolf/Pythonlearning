#plaindrome are the kind of string  which are same from left or right whichever way you read them. Example "madam". in this example we will take the word as input from the user and say if it is plaindrome or not

s = input("Please enter a string: ")

z = s[::-1]
if s == z:
    print("The string is plaindrome")

else:
    print("The string is not plaindrome")
