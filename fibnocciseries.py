#Let us try to solve Fibonacci series. in this series we get the next number by adding the previous two numbers like 1,1,2,3,5,8,13....

a, b = 0, 1

while b < 100:
    print (b)
    a, b = b, a + b 
