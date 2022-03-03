#ASSINGMENT
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

operation = input(''' Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for devition
''')

#Addition
if operation == '+':
    print('{} + {} = '.format(number_1,  number_2))
    print(number_1 + number_2)

#Subtraction
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

#Multiplication
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

#Division
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
    
#while True:
   # a = input("Enter yes/no to continue: ")
    #if a=="yes":
     #   continue
    #elif a=="no":
        #break
while input("Do you want to continue? [y/n]") == 'y':
    print ("continue")
    

else:
    print("You have not typed a valied operator, please run the program again.")
