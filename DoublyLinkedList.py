'''
Doubly linked list
'''

class _DoublyLinkedBase:

    # double link node
    class _Node:
        __slots__='_element','_prev','_next'

        def __init__(self,element,previous,next):
            self._element=element
            self._prev=previous
            self._next=next

    def __init__(self):
        # Here we use sentinels
        self._head=self._Node(None,None,None)
        self._tail=self._NOde(None,self._head,None)
        self._head._next=self._tail
        self._size=0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0

    def _insert_between(self,e,predecessor,successor):
        e=self._Node(e,predecessor,successor)
        predecessor._next=e
        successor._prev=e
        return e

    def _delete_node(self,node):
        pred=node._prev
        succ=node._next
        pred._next=succ
        succ._prev=pred
        ans=node._element
        node._prev=node._next=node=None
        return ans

    def _replace(self,e,node):
        old=node._element
        node._element=e
        return old

class PositionalList(_DoublyLinkedBase):

    class Position:

        def __int__(self,container,node):
            self._container=container
            self._node=node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node

        def __ne__(self, other):
            return not (self == other )

    def _validate(self,p):
        if p._container is not self:
            raise ValueError("P is not in the list!")
        if not isinstance(p,self.Position):
            raise TypeError("P is invalid!")
        if p._node._next is None:
            raise ValueError("P is not in the list any longer!")
        return p._node

    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)

    #　Position is like a cursor

    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def after(self,p):
        pos=self._validate(p)
        return self._make_position(pos)
    def before(self,p):
        pos=self._validate(p)
        return self._make_position(pos)
    def __iter__(self):
        if self._size>0:
            cursor=self.first()
            while cursor is not None:
                yield cursor.element()
                cursor=self.after(cursor)
    # mutate

    def _insert_between(self,e,predecessor,successor):
        pos=super()._insert_between(e,predecessor,successor)
        return self._make_position(pos)
    def add_first(self,e):
        return self._insert_between(e,self._head,self._head._next)
    def add_last(self,e):
        return self._insert_between(e,self._tail._prev,self._tail)
    def add_before(self,e,p):
        node=self._validate(p)
        return self._insert_between(e,node._prev,node)
    def add_after(self,e,p):
        node=self._validate(p)
        return self._insert_between(e,node,node._next)
    def delete(self,p):
        node=self._validate(p)
        return self._delete_node(node)
    def replace(self,e,p):
        node=self._validate(p)
        old=node._element
        node._element=e
        return old




