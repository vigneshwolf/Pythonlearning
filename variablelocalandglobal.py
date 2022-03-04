# To understand local and global variable we will go through two examples
def change(a):
    a = 10
    print(f"Inside of the change function {a}")

a = 9
print(f"Before the function call {a}")
change(a)
print(f"After the function call {a}")

def change(b):
    global a
    a = 10
    print (a)

a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change(a)
print("After the function call ", a)
