class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                return

    def createCSLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        return 'Circular Singly Linked List is Created'

    def insert(self, value, idx):
        if self.head is None:
            return 'The head reference is none'
        else:
            node = Node(value)
            if idx == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif idx == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < idx - 1:
                    temp = temp.next
                    index += 1
                nextnode = temp.next
                temp.next = node
                node.next = nextnode
                return 'The node has been successfully inserted'


csll = CircularSinglyLinkedList()
csll.createCSLL(1)

print([node.value for node in csll])

print(csll.insert(0, 0))
csll.insert(3, -1)
csll.insert(2, 2)
csll.insert(4, -1)

print([node.value for node in csll])
