# also remember that default value is elevated only once, so if you have any mutable object like this it will make a diffrence. see the next example

def f(a, data=[]):
    data.append(a)
    return data
print(f(1))

print(f(2))

print(f(3))

