class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initialize a new head for the linked list
head = None

# Detect if there is a loop in the linked list
def detectLoop(head):
    a = head
    b = head

    while a is not None and b is not None and b.next is not None:
        a = a.next
        b = b.next.next
        if a == b:
            return True

    return False

# Inserting new values
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Adding a loop for the sake of this example
temp = head
while temp.next is not None:
    temp = temp.next

temp.next = head

# Check if a loop exists
if detectLoop(head):
    print("Loop exists in the Linked List")
else:
    print("Loop does not exist in the Linked List")
