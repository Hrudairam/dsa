#write a code to demonistarte stck operations
stack=[]
stack.append(10)
stack.append(11)
stack.append(55)
stack.append(22)
stack.append(12)
print("stack after pushing:",stack)
deleted = stack.pop()
print("stack after poping 1 time :", stack)
deleted = stack.pop()
print("stack after popping 2 times :",stack)
print("stack element ready to be popped:",stack[-1])
print("reamining size of the stack :",len(stack))
