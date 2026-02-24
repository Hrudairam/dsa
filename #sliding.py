#sliding
#write a code to get the maximum size of a substring which has vowel, where window size is constant 3
s=input("enter a string:")
k=int(input("enter window size:"))
def max_vowels(s,k):
    vowels= 'aeiouAEIOU'
    count= 0
    for i in range (k):
        if s[i] in vowels:
            count+=1    
    max_count=count
    for i in range(k,len(s)):
        if s[i] in vowels:
            count+=1
    max_count=count
    for i in range(k,len(s)):
        if s[i] in vowels:
            count+=1
        if s[i-k] in vowels:
            count-=1
        max_count= max(max_count,count)
    return max_count
print("maximum vowels substring size is",max_vowels(s,k))



