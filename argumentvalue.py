# In a function variables may have default arguments values, that means if we dont give ny value for that particular variable it will be assigend automatically.

def test(a , b=-99):
    if a > b:
        return True
    else:
        return False
    print (test(a))
