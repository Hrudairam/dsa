#write a code to arrange the given number in the list to form a largest number 
'''example:[3,30,34,5,9]'''
from functools import cmp_to_key
def compare(a,b):
    if a+b > b+a:
        return-1
    else:
        return 1
arr=list(map(str,input("enter elements").split()))
arr.sort(key=cmp_to_key(compare))
print("".join(arr))