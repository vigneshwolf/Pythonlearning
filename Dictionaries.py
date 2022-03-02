# Dictionaries are unorder ser of key:value paris where keys are unique. we declare dictionaries using {} braces. we use dictionaries to store data for any particular key and then retrive them.

data = {'name' : 'vignesh', 'age_' : '25', 'state' : 'Tamilnadu'}
print(data)
print (data['age_'])

# we can add more data to it by simply

data['city'] = 'chennai'
print (data)

# To delete any perticular key:value pair

del data['name']
print (data)
