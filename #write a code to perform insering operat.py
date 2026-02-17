#write a code to perform insering operation in singly linked list
class node:
    def __init__(self, data):
        self .data= data
        self .next= None
def insert_at_end(head, value):
    new_mode= node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp= temp.next
    temp.next= new_node
    return head
def _print_list(head):
    temp= head 
    while temp:
        print(temp.data, end= "->")
        temp= temp.next
    print("Tail")
head =None
n=int(input("enter number of elements:"))
for i in range(n):
    val= int (input("enter a value:"))
    head=insert_at_end(head, val)
print("singly linked list :",_print_list(head))
    
       
