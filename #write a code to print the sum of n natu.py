#write a code to print the sum of n natural numbers using linear recursion
def linear(n):
    if n==0:
        return 0
    return n+linear(n-1)
n=int(input("enter n:"))
print("sum:",linear(n))