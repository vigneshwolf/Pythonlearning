# This also happens whn you pass them into functions. for example, in the below function, we are passing a list, and appending new numbers into it. This is also changes the variable outside of the function.

numbers = [1, 2, 3]
def modify(numbers):
    numbers.append (42)
    
modify(numbers)
print(numbers)
