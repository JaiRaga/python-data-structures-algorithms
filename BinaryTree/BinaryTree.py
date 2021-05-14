class BinaryTree:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self, node):
        self.children.append(node)


tree = BinaryTree('Drinks', [])
cold = BinaryTree('Cold', [])
hot = BinaryTree('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = BinaryTree('tea', [])
coffee = BinaryTree('coffee', [])
cola = BinaryTree('Cola', [])
fanta = BinaryTree('fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)
