#write a code to create a stack using a class and access the elements in the stack
class stack:
    def __init__(self):
        self.stack= []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack)==0:
            return "stack Empty......."
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "Stack Empty......."
        return self.stack[-1]
    def display(self):
        return self.stack
s=stack()
s.push(2)
s.push(22)
s.push(222)
s.push(2222)
print("stack",s.display())
print("pop:",s.pop())
print("peek",s.peek())