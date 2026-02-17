class node:
    def _init_(self,data):
        self.data=data
        self.next=None
def insert_at_end(head,value):
    new_node=node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
        temp.next=new_node
        return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("tail")
head=None
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    head=insert_at_end(head,val)
print("singly linked list:",print_list(head))