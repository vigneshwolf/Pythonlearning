# let us write a program to eveluate the power series. the series looks like e**x=1+x+x**2/2!+x**3/3!+....+x**n/n! where 0<x<1

x = float(input("Enter the value of X: "))
n = term = num = 1
sum = 1.0
while n <= 100:
    term *= x / n
    sum += term
    n += 1
    if term < 0.0001:
        break
    print("No of Times= %d and sum= %f" % (n, sum)) 
