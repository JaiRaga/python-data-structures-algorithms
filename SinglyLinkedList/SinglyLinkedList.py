class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # time complexity ==> o(n)
    # space complexity ==> o(1)
    def insert(self, value, index):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            if index == 0:
                node.next = self.head
                self.head = node
            elif index == -1:
                self.tail.next = node
                self.tail = node
            else:
                target = self.head
                count = 0

                while count < index - 1:
                    target = target.next
                    count += 1
                temp = target.next
                target.next = node
                node.next = temp
                if target == self.tail:
                    self.tail = node

    # time complexity ==> o(n)
    # space complexity ==> 0(1)
    def traverse(self):
        node = self.head
        if node is None:
            return
        while node is not None:
            print(node.value)
            node = node.next


sll = SinglyLinkedList()
sll.insert(1, 1)
sll.insert(2, -1)
sll.insert(3, -1)
sll.insert(4, -1)
sll.insert(0, 0)
sll.insert('g', 3)

sll.traverse()

print([node.value for node in sll])
