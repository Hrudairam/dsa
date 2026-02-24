#write a code deletion operation in class node
class node:
  def __init__(self, data):
    self.data=data
    self.left=None
    self.right=None
def insert(root, val):
  if root is None:
    return node(val)
  if val < root.data:
    root.left=insert(root.left, val)
  else:
    root.right=insert(root.right, val)
  return root
def delete(root, val):
  if root is None:
    return None
  if val < root.data:
    root.left=delete(root.left, val)
  elif val > root.data:
    root.right=delete(root.right, val)
  else:
    if root.left is None:
      return root.right
    if root.right is None:
      return root.left
    temp=root.right
    while temp.left:
      temp=temp.left
    root.data=temp.data
    root.right=delete(root.right, temp.data)
  return root 
def inorder(root):
  if root:
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
values=list(map(int, input("Enter elements:").split()))
root=None
for v in values:
  root=insert(root, v)
print("Before delete")
inorder(root)
key=int(input("Enter value to delete:"))
root=delete(root, key)
print("After delete:")
inorder(root)