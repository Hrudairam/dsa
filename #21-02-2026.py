#21-02-2026
def lst(s):
    left = max_len=start=0
    seen={}
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >=left:
            left= seen[s[right]]+1
        seen[s[right]]=right
        c_len= right-left+1
        if c_len >max_len:
            max_len=c_len
            start=left
    return s[start:start+max_len]
s=input("enter a string: ")
print("longest unique substring :",lst(s))