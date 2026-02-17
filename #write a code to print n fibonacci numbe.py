#write a code to print n fibonacci numbers 
def tree(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter range:"))
for i in range(n):
    print(fib(i),end=' ')