# Remember the plaindrome program we wrote in the last chapter. let us write a function which will check if a given string is plaindrome or not, then return True or False.

def plaindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    if plaindrome(s):
        print("yay a plaindrome")
    else:
        print("oh no, not a plaindrome")
