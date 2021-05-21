class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


linkedlistBT = BinaryTree('Drinks')
leftChild = BinaryTree('Hot')
rightChild = BinaryTree('Cold')
left1SubChild = BinaryTree('Tea')
left2SubChild = BinaryTree('Coffee')
right1SubChild = BinaryTree('Cola')
right2SubChild = BinaryTree('Fanta')
linkedlistBT.leftChild = leftChild
linkedlistBT.rightChild = rightChild
leftChild.leftChild = left1SubChild
leftChild.rightChild = left2SubChild
rightChild.leftChild = right1SubChild
rightChild.rightChild = right2SubChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


preOrderTraversal(linkedlistBT)

print('-----------------------------------------------')


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


inOrderTraversal(linkedlistBT)

print('-----------------------------------------------')


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


postOrderTraversal(linkedlistBT)
