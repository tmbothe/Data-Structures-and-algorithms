class Node:

    def __init__(self, data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root =Node(data,None)
        else:
            self.insert_node(data,self.root)
    
    def insert_node(self,data,node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        else:
            if node.rightChild:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild = Node(data,node)


    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self,node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print(f'current: {node.data}')

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self,node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self,node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

  



    




if __name__=='__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(66)
    bst.insert(-5)
    bst.insert(1)
    bst.insert(99)
    bst.insert(34)
    bst.insert(32)
    bst.insert(11)
    bst.insert(0)
    bst.insert(100)

    bst.traverse()
    print(f'Max value : {bst.get_max_value()}')
    print(f'Min value : {bst.get_min_value()}')