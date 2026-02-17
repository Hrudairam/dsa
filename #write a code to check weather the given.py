#write a code to check weather the given number is even or not using indirect function
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
n=int(input("enter a number :"))
print("even:",is_even(n))
