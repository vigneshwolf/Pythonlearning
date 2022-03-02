# you may also need to iterate through two sequence same time, for that zip() function.

a = ['name', 'city']
b = ['vignesh', 'chennai']

for x, y in zip (a, b):
    print("%s uses %s" % (x, y))
