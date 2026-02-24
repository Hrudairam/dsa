#sort by absolute values 
arr=list(map(int,input("enter elements:").split()))
print(sorted(arr,key=abs))