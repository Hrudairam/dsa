#Write a code to generate all the combinatinons while permuting a string using the backteacking in a recursion
def combine(s,ans=' '):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        ch= s[i]
        left_over=s[:i]+s[i+1:]
        combine(left_over,ans+ch)
s=input("enter a string:")
combine(s)