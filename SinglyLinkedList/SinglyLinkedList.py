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

    # time complexity ==> o(n)
    # space complexity ==> o(1)
    def search(self, value):
        if self.head is None:
            print('The linked list is empty.')
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return 'The value does not exist in the sll.'

    # Deletes a node
    # time complexity ==> o(n)
    # space complexity ==> o(1)
    def delete(self, index):
        if self.head is None:
            print('SLL is empty.')
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif index == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp = self.head
                ind = 0

                while ind < index - 1:
                    temp = temp.next
                    ind += 1
                nextNode = temp.next
                temp.next = nextNode.next

    # Deletes the entire SLL
    # time complexity ==> o(1)
    # space complexity ==> o(1)
    def deleteSLL(self):
        if self.head is None:
            print('SLL is empty.')
        else:
            self.head = None
            self.tail = None


sll = SinglyLinkedList()
sll.insert(1, 1)
sll.insert(2, -1)
sll.insert(3, -1)
sll.insert(4, -1)
sll.insert(0, 0)
sll.insert('g', 3)

sll.traverse()

sll.search(3)

print([node.value for node in sll])
sll.delete(3)
sll.deleteSLL()
print([node.value for node in sll])
