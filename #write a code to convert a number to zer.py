#write a code to convert a number to zero using nested recursion
def timer(n):
    if n<=0:
        return 0
    return timer(timer(n-1))
n=int(input("Enter a number:"))
print(timer(n))