class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


sll = SinglyLinkedList()
n1 = Node(1)
n2 = Node(2)

sll.head = n1
sll.head.next = n2
sll.tail = n2
