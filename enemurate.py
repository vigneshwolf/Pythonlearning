# if you want to loop through a list (or any sequence) and get iteration number at the same time you have to use enumerate().

for i, j in enumerate(['a', 'b', 'c'], start=1): 
    print (i, j)
