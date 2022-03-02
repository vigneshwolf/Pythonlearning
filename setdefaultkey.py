# Many times it happens that we want to add more data to a value in a dictonary and if the key does not exists then we add some default value. you can do this efficiently using dict.setdefault(key,default).

data = {}
data.setdefault('name' , []).append('vignesh')
print(data)
data.setdefault('state' , []).append('Tamilnadu')
print(data)
data.setdefault('city' , []).append('chennai')
print(data)
