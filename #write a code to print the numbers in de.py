#write a code to print the numbers in descending order using a function tools comparitve key
from functools import cmp_to_key
def compare(a,b):
    if a>b:
        return -1
    elif a<b:
        return 1
    else:
        return 0
arr=list(map(int,input("elements:").split()))
print(sorted(arr, key=cmp_to_key(compare)))