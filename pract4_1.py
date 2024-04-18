class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._recursive_insert(data, self.root)

    def _recursive_insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._recursive_insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._recursive_insert(data, current_node.right)

    def min(self):
        if self.root is None:
            print('Tree is empty')
            return
        node = self.root

        while node.left is not None:
            node = node.left
        return node.data

    def max(self):
        if self.root is None:
            print('Tree is empty')
            return
        node = self.root

        while node.right is not None:
            node = node.right
        return node.data

    def __contains__(self, data):
        if self.root is None:
            print('Tree is empty')
            return
        node = self.root

        while node:
            if node.data == data:
                return True
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return False  # Не знайдено

    def print(self):
        if self.root is None:
            print('Tree is empty')
            return
        self._inoder(self.root)

    def _inoder(self, node):
        if node is not None:
            self._inoder(node.left)
            print(node.data, end=' ')
            self._inoder(node.right)
            print()


tree = BinaryTree()
tree.insert(3)
tree.insert(2)
tree.insert(8)
tree.insert(11)
tree.insert(1)
print(4 in tree)
tree.print()