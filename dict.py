# You must remember that no mutable object can be a key. that means you can not use a list as a key. dict() can create dictionaries from tuples of key ,values pair.

a = dict((('name' , 'vignesh') , ('city' , 'chennai')))
print (a) 
