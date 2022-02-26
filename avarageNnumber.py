#we will do an avarage of N number

N = 10
sum = 0
count = 0
while count < N:
    number = float(input(""))
    sum = sum + number
    count = count +1
avarage = float(sum) / N
print("N = %d , sum + %f" % (N, sum))
print("Avarage = %f" % avarage)
