# f-string provides a simple and readable way to embed python expression in a string.
answer = 42
print(f"The answer is {answer}")
import datetime
d = datetime.date(2021, 2, 26)
print (f"{d} was a {d:%A}, we started the mailing list back then.")
