# to avoide this you can write more idiomatic python, like the following.

def f(a, data=None):
    if data is None:
        data = []
        data.append(a)
        return data

print(f(1))

print(f(2))
