class Empty(Exception):
    pass


class BinaryTreeBase:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left, right):
            self._element = element
            self._right = right
            self._left = left

    def __init__(self):
        self._root = None

    def clear(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        if self.is_empty():
            raise Empty("The tree is empty!")
        return self._root

    def remove(self, e):
        raise NotImplementedError("The method is not valid without upperclass!")

    def insert(self, e):
        raise NotImplementedError("The method is not valid without upperclass!")

    def contain(self, e):
        raise NotImplementedError("The method is not valid without upperclass!")

    def findMin(self, e):
        raise NotImplementedError("The method is not valid without upperclass!")

    def findMax(self, e):
        raise NotImplementedError("The method is not valid without upperclass!")

    def height(self):
        raise NotImplementedError("The method is not valid without upperclass!")

    def printTree(self):
        raise NotImplementedError("The method is not valid without upperclass!")


class BinarySearchTree(BinaryTreeBase):
    def __init__(self):
        super().__init__()

    def left(self, node):
        return node._left

    def right(self, node):
        return node._right

    def _insert(self, e, node):
        if node is None:
            return self._Node(e, None, None)

        else:
            if e > node._element:
                node._right = self._insert(e, node._right)
            elif e < node._element:
                node._left = self._insert(e, node._left)
            else:
                None

        return node

    def _findMax(self, node):
        if node is None:
            return None
        if node._right is None:
            return node
        else:
            return self._findMax(node._right)

    def _findMin(self, node):
        if node is None:
            return None
        if node._left is None:
            return node
        else:
            return self._findMin(node._left)

    def _remove(self, e, node):
        if e < node._element:
            node._left = self._remove(e, node._left)
        elif e > node._element:
            node._right = self._remove(e, node._right)
        elif node._right is not None and node._left is not None:
            node._element = self._findMin(node._right)._element
            node._right = self._remove(node._element, node._right)
        else:
            node = node._left if node._left is not None else node._right

        return node

    def _contain(self, e, node):
        if node is None:
            return False

        if e == node._element:
            return True
        elif e < node._element:
            return self._contain(e, node._left)
        else:
            return self._contain(e, node._right)

    def insert(self, e):
        self._root = self._insert(e, self._root)

    def findMax(self):
        return self._findMax(self._root)._element

    def findMin(self):
        return self._findMin(self._root)._element

    def contain(self, e):
        if self.is_empty():
            raise Empty("The tree is empty!")
        return self._contain(e, self._root)

    def remove(self, e):
        if not self.contain(e):
            raise ValueError("The tree does not contain such a value!")

        self._root = self._remove(e, self._root)

    def _inorder(self, node):
        if node._left is not None:
            for object in self._inorder(node._left):
                yield object
        yield node
        if node._right is not None:
            for object in self._inorder(node._right):
                yield object

    def printTree(self):
        print('The inorder traversal of the tree is shown beloww:')
        if self.is_empty():
            raise Empty('The tree is Empty!')
        nodes = self._inorder(self._root)
        for i in nodes:
            print(i._element, end=" ")
        print(end='\n')


if __name__ == '__main__':
    test = BinarySearchTree()
    items = 5, 4, 7, 2, 6, 10, 1, 3, 9, 15
    for i in items:
        test.insert(i)
    test.printTree()
    test.contain(10)
    test.findMin()
    test.findMax()
    test.remove(10)
    test.printTree()
    test.insert(10)
    test.printTree()


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = self._Node(None, None)
        self._tail = self._Node(None, None)
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def dequeue(self):
        if self.is_empty():
            raise Empty("The Queue is empty!")
        oldHead = self._head._next
        self._head._next = oldHead._next
        val = oldHead._element
        oldHead = None
        self._size -= 1
        return val

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head._next = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("The Queue is empty!")
        return self._head._next._element


if __name__ == '__main__':
    test2 = LinkedQueue()
    for i in range(10):
        test2.enqueue(i)
    test2.top()
    len(test2)
    for i in range(10):
        test2.dequeue()
    try:
        test2.dequeue()
    except Empty:
        print("Empty warning!")


class BinaryPrintTree(BinarySearchTree):
    def _preorder(self, node):
        yield node
        if node._left is not None:
            for object in self._preorder(node._left):
                yield object
        if node._right is not None:
            for object in self._preorder(node._right):
                yield object

    def printTreeP(self):
        if self.is_empty():
            raise Empty("The Tree Is Empty!")
        nodes = self._preorder(self._root)
        print("The Preorder sequence is:")
        for i in nodes:
            print(i._element, end=' ')
        print(end='\n')

    def _postorder(self, node):
        if node._left is not None:
            for object in self._postorder(node._left):
                yield object
        if node._right is not None:
            for object in self._postorder(node._right):
                yield object
        yield node

    def printTreePo(self):
        if self.is_empty():
            raise Empty("The Tree Is Empty!")
        nodes = self._postorder(self._root)
        print("The Postorder sequence is:")
        for i in nodes:
            print(i._element, end=' ')
        print(end='\n')

    def _breathfirst(self):
        Q = LinkedQueue()
        Q.enqueue(self._root)
        while not Q.is_empty():
            new = Q.dequeue()
            yield new
            if new._left is not None:
                Q.enqueue(new._left)
            if new._right is not None:
                Q.enqueue(new._right)

    def printTreeB(self):
        if self.is_empty():
            raise Empty("The Tree Is Empty!")
        nodes = self._breathfirst()
        print("The BreathFirst sequence is:")
        for i in nodes:
            print(i._element, end=' ')
        print(end='\n')


if __name__ == '__main__':
    test3 = BinaryPrintTree()
    items = 5, 4, 7, 2, 6, 10, 1, 3, 9, 15
    for i in items:
        test3.insert(i)
    test3.printTreeP()
    test3.printTreePo()
    test3.printTreeB()

'''
Expression Tree
'''


# ________________ExpressionTree: subclass of BinarySearchTree_________________#
class ExpressionTree(BinarySearchTree):
    def _attach(self, node, left, right):
        if node._left is not None and node._right is not None:
            raise ValueError("The node should be a leaf!")
        if left is not None:
            node._left = left._root
            left._root = None
        if right is not None:
            node._right = right._root
            right._root = None

    def __init__(self, e, left=None, right=None):
        super().__init__()
        self._root = self._Node(e, None, None)
        if not (left is None or right is None):
            self._attach(self._root, left, right)
        elif left is None or right is None:
            self._attach(self._root, left, None) if left is not None else self._attach(self._root, None, right)
        else:
            None


# ________________over__________________________________________________________#

# __________________LinkedStack_______________________________________________#
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = self._Node(None, None)
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head._next = new
        else:
            new._next = self._head._next
            self._head._next = new
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("The Stack is Empty!")
        old = self._head._next
        self._head._next = old._next
        val = old._element
        old = None
        self._size -= 1
        return val

    def top(self):
        if not self.is_empty():
            return self._head._next._element
        return None

    def __len__(self):
        return self._size


# _______________________linkedStack_test______________________________________#
if __name__ == '__main__':
    s = LinkedStack()
    for i in range(10):
        s.push(i)
    s.is_empty()
    s.top()
    for i in range(10):
        s.pop()
    s.pop()
    len(s)


# ______________________BuildTree______________________________________________#
def buildTree(sr):
    s = LinkedStack()
    if not isinstance(sr, str):
        raise ValueError("The Value you put is not valid!")
    for i in sr:
        if i in "+-*/":
            s.push(i)
        elif i not in '()':
            s.push(ExpressionTree(i))
        elif i is ')':
            right = s.pop()
            operator = s.pop()
            left = s.pop()
            s.push(ExpressionTree(operator, left, right))
    return s.pop()


# ________________________TEST_________________________________________________#
if __name__ == '__main__':
    x = buildTree('(((3+5)*8)/9)')
    x2 = buildTree('((3+5)*8)/((9-2)*7))')
    x.printTree()
    x2.printTree()
# __________________Calculate_Expression_Tree__________________________________#






