class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, value):

        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    elements = [99, 1, 5, 3, 7, 8, 12, 14, 13, 17, 2, 91, 56, 73, 92, 92, 92, 92, 49]
    num_tree = build_tree(elements)
    print('In order traversal gives {} sorted element.'.format(num_tree.in_order_traversal()))
    print('The number {} is present : {} '.format(90, num_tree.search(90)))

