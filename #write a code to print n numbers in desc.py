#write a code to print n numbers in descending order using direct function
def direct(n):
    if n==0:
        return
    print(n)
    direct(n-1)
n=int(input("enter a number :"))
direct(n)