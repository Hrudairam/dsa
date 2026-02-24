#code to demonistrate a binary search tree conversion in to a inorder travelsel and print the traversed path
class node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None
def insert(root, value):
    if root is None:
        return node(value)
    if value<root.data:
        root.left=insert(root.left, value)
    else:
        root.right=insert(root.left,value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
values = list(map(int,input("enter elements :").split()))
root= None
for v in values:
    root = insert(root,v)
print(inorder(root))

