'''
this is the base for a binary search tree
'''


class BinarySearchBase:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left, right):
            self._element = element
            self._left = left
            self._right = right

    def _contains(self, e, node):
        # recursively
        if node is None:
            return False

        if e < node._element:
            return self._contains(e, node._left)
        elif e > node._element:
            return self._contains(e, node._right)
        else:
            return True

    def _findMin(self, node):

        if node is None:
            return None
        elif node._left is None:
            return node

        return self._findMin(node._left)

    def _findMax(self, node):
        if node is None:
            return None
        elif node._right is None:
            return node
        return self._findMax(node._right)

    def _insert(self, e, node):
        # this step is a little tricky
        if node is None:
            return self._Node(e, None, None)

        if e < node._element:
            node._left = self._insert(e, node._left)
        elif e > node._element:
            node._right = self._insert(e, node._right)
        else:
            None

        return node #To make sure the node already exist does not change
    def _remove(self,e,node):
        if node is None:
            return None

        if e < node._element:
            node._left=self._remove(e,node._left)
        elif e > node._element:
            node._right=self._remove(e,node._right)
        elif node._left is not None and node._right is not None:
            # this is the case where the node to be deleted have two children
            node._element=self._findMin(node._right)
            node._right=self._remove(node._element,node._right)
        else:
            node=node._left if node._left is not None else node._right

        return node
raise Over
