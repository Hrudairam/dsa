#write a code to print a number in a fibonnaci series using its index by tree recursion
def tree(n):
    if n<=1:
        return n
    return tree(n-1)+tree(n-3)
n=int(input("enter index:"))
print("fibo:",tree(n))

