from BinaryTreeBase import BinaryTree as BinaryTree
'''
Here is a Tree ADT base
'''
from QueueT import LInkedQueue as Queue

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__='_element', '_parent', '_left', '_right'
        def __init__(self,element,parent,left,right):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    class Position(BinaryTree.Position):

        def __init__(self,container,node):
            self._container=container
            self._node=node

        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(self) is type(other) and other._node is self._node
        def __ne__(self, other):
            return not self==other

    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("Input is not valid!")
        if p._container is not self:
            raise ValueError("Input is not in the tree!")
        if p._node._parent is p._node:
            raise ValueError("Input is no longer valid!")
        return p._node
    def _make_position(self,node):
        return self.Position(self,node) if node is not None else None

    #----------------------tree--------------------#
    def __init__(self):
        self._root=None
        self._size=0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node=self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        node=self._validate(p)
        count=0
        if node._left is not None:
            count +=1
        if node._right is not None:
            count +=1
        return count
    #-------------operations------------------
    def _add_root(self,e):
        if self._root is not None:
            raise ValueError("Root exists!")
        self._size +=1
        self._root=self._Node(e,None,None,None)
        return self._make_position(self._root)
    def _add_left(self,p,e):
        node=self._validate(p)
        if node._left is not None:
            raise ValueError("Left exists!")
        self._size +=1
        node._left = self._Node(e,node,None,None)
        return self._make_position(node._left)
    def _add_right(self,p,e):
        node=self._validate(p)
        if node._right is not None:
            raise ValueError("Right exists!")
        self._size +=1
        node._right=self._Node(e,node,None,None)
        return self._make_position(node._right)
    def _replace(self,p,e):
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        '''
        Delete the node at Position P, and replace it
        with its child, if any
        :param p:
        :return: the element stored in p
        or raise ValueError if p has 2 children or
        p is not valid.
        '''
        node=self._validate(p)
        if self.num_children(p)==2:
            raise ValueError("It has two children!")
        # Here is a trick
        # a=3;b=None; c= b if b else 3 __ c=3
        # None
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size -=1
        node._parent=node
        return node._element
    def _attach(self,p,t1,t2):
        node=self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf!')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match!')
        self._size += len(t1)+len(t2)
        if not t1.is_empty():
            t1._root._parent=node
            node._left=t1._root
            t1._root=None
            t1._size=0
        if not t2.is_empty():
            t2._root_parent=node
            node._right=t2._root
            t2._root=None
            t2._size =0
    #__________TreeTraversals in Python ____________#

    def __iter__(self):
        for p in self.positions():
            yield p.element()
    '''
    Here is the implement written by myself:
    most of them are incorrect
    '''
    def positions(self, start=self.root(),method='preorder'):
        methods='preorder','postorder','breadth-first','inorder'
        if method not in methods:
            raise ValueError("The method you called is not supported!")
        if method=='preorder':
            if start is self.root():
                yield start
            if self.is_leaf(start) :
                return None
            else:
                for child in self.children(start):
                    yield child
                    self.postions(child)
        if method=='postorder':
            for child in self.children(start):
                if self.is_leaf(child):
                    yield child
                else:
                    self.positions(child)
                    yield child
        if method=='inorder':
            if self.left(start) is not None:
                lt=self.left(start)
                self.positions(lt)
            yield start

            if self.right(start) is not None:
                rt=self.right(start)
                self.positions(rt)

        if method=='breadthfirst':
            Q=Queue()
            Q.enqueue(start)
            while not Q.is_empty():
                Nroot=Q.dequeue()
                yield Nroot
                if not self.is_leaf(Nroot):
                    for child in self.children(Nroot):
                        Q.enqueue(child)
    '''
    From book -> to fill here
    '''
    def search_binary(self,e,startP=self.root()):
        ## Need to fix the problem None._node._element
        if startP._node._elment==e:
            return startR
        elif startP._node._elment<e:
            self.search_binary(self.left(startP))
        else:
            self.search_binary(self.right(startP))
        print("Nothing found!")





