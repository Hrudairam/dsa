# write code to reverse a string using a stack
text=input("enter a string: ")
stack=[]
for ch in text:
    stack.append(ch)
rev_string=" "
while stack:
    rev_string+=stack.pop()
print("Reversed string : ", rev_string)