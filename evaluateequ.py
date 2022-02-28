# This is a program to evaluate 1/x+1(x+1)+1/(x+2)+...+1/n series upto n, in our case x=1 and n=10

sum = 0.0
for i in range(1,11):
    sum += 1.0 / i
    print("%2d %6.4f" % (i , sum))
    
