# if the value of expression is true (anything other than zero), do the what is written  below under the int(integer). One simple example is to take some numbers as input and check if the number is less than 100 or not.

#Now in the above exapmle we want to print "greater than" if the number is greater than 100. For that we have to use the else statement. this works when the if statement is not fulfilled.

number = int(input("Enter the number: "))
if number < 100:

    print("The number is less than 100")
else:
    print("The number is greater than 100")
