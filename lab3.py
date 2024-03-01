class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        ######## YOUR CODE STARTS HERE ######
        self.root = None

    def insert(self, value):
        ######## YOUR CODE STARTS HERE ######
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._insert_recursive(current.left, value)

    def delete(self, value):
        ######## YOUR CODE STARTS HERE ######
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                current.value = self._find_successor(current.right).value
                current.right = self._delete_recursive(current.right, current.value)
        return current

    def _find_successor(self, current):
        while current.left is not None:
            current = current.left
        return current

    def find(self, value):
        ######## YOUR CODE STARTS HERE ######
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self):
        ######## YOUR CODE STARTS HERE ######
        output = []

        self._inorder_recursive(self.root, output)
        return output

    def _inorder_recursive(self, current, output):
        if current is not None:
            self._inorder_recursive(current.left, output)
            output.append(current.value)
            self._inorder_recursive(current.right, output)
