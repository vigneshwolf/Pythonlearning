# We can use rjust or ljust methods to either right justify or left justify any given strings. we have to provide the number of characters we want to justify, and the character we want use for the justification (while a whitespace too).

i = "ABCD".rjust(10,"-")
print (i)

u = "ABCD".ljust(10,"-")
print (u)
