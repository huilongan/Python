from BinarySearchTree import BinarySearchBase as BinarySearchBase

class BinarySearchTree(BinarySearchBase):

    def __init__(self):
        self._root=None

    def root(self):
        return self._root

    def clear(self):
        self._root = None
    def is_empty(self):
        return self._root is None

    def contains(self,e):
        return self._contains(e,self.root())
    def findMin(self):
        return self._findMin(self.root())._element
    def findMax(self):
        return self._findMax(self.root())._element

    def insert(self,e):
        self._root=self._insert(e,self._root)
    def remove(self,e):
        if self.contains(e):
            return self._remove(e,self.root())
        else:
            raise ValueError('The input is not in the tree!')

    def inorder(self):
        return self._inorderTra(self._root)
    def _inorderTra(self,node):
        if node is None:
            None
        else:
            if node._left is not None:
                self._inorderTra(node._left)
            yield node
            if node._right is not None:
                self._inorderTra(node._right)
test=BinarySearchTree()
for i in range(10):
    test.insert(i)




