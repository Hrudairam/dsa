# write a code to check an expression to balance 
exp= input("Enter an expression:")
stack=[]
balanced= True
for ch in exp:
    if ch in '([{':
        stack.append(ch)
    elif ch in '}])':
        if not  stack:
            balanced = False
            break
        top= stack.pop()
        if (ch==')'and top !='(' or ch=='{' and top !='}' or ch=='[' and top !=']'):
            balanced=False
            break
if balanced and not stack:
    print("balanced")
else:
    print("Not")