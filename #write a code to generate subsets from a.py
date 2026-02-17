#write a code to generate subsets from a list using simple back tracking of a recursion
def sset(arr, index=0, current=[]):
    if index==len(arr):
        print(current)
        return
    sset(arr, index+1, current+[arr[index]])
    sset(arr, index+1, current)
arr=list(map(int,input("enter nus with space:").split()))
sset(arr)