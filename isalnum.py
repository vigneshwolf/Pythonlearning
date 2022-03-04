# Because of the spaces in the first line isalnum() returned as false, it checkes for all the charecters  are in alphabets numeric or not.

s = "jdwb 23232njm"
s = s.isalnum()
print (s)

s = "jdwb23232njm"
s = s.isalnum()
print(s)
