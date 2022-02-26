#We will convert the given temperature to celcius from faranheit by using the formula C=(F-32)/1.8

fahrenhiet = 0.0
print("Fahrenhiet celsius")
while fahrenhiet <= 250:
    celsius = (fahrenhiet - 32.0) / 1.8 #Here we calculate the celsius value.
    print("%5.1f %7.2f" % (fahrenhiet, celsius))
    fahrenhiet = fahrenhiet + 25
