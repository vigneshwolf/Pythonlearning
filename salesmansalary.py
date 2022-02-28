# In this exapmle we are going to calculate the salary of a camera salesman. His basic salary is 1500 for example, for every camera he will sell he will get 200 and the camera commision on the month's sales is 2%. The input will be number of cameras sold and total price if the camera.

basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(input("Enter the number of input sold: "))
price = float(input("Enter the total price: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print("Bonus = %4.2f" % bonus)
print("commision = %4.2f" % commision)
print("Gross salary = %4.2f" % (basic_salary + bonus + commision))
