#wirte a code to print n values using head recursion
def head(n):
    if n==0:
        return
    head(n-1)
    print(n)
n=int(input("enter a number:"))
head(n)