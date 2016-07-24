'''
To review the singly linked list
'''

#SinglyLinkedList
class Empty(Exception):
    pass

class SinglyLinkedBase:

    class _Node:
        __slots__='_element','_next'

        def __init__(self,element,next):
            self._element= element
            self._next=next

    def __init__(self):
        # sentinels
        self._head=self._Node(None,None)
        self._tail=self._Node(None,None)
        self._head._next=self._tail
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0
    # for a singlyLinkedList, the only thing we know is the node after one particular node
    # so, all the insertion or deletion operations should base on the previous node
    def _insert_after(self,e,predecessor):
        new=self._Node(e,predecessor._next)
        predecessor._next=new
        self._size +=1
        return new


    def _delete_after(self,predecessor,node):
        predecessor._next=node._next
        ans=node._element
        node=None
        self._size -=1
        return ans
    def _replace(self,e,node):
        old=node._element
        node._element=e
        return old
# C-7.27


# stack based on the singlyLinkedList

class SinglyLinkedStack(SinglyLinkedBase):



    def push(self,e):
        self._insert_after(e,self._head)

    def pop(self):
        return self._delete_after(self._head,self._head._next)

    def top(self):
        if self._size==0:
            raise Empty("The queue is empty!")
        return self._head._next._element

if __name__=='__main__':
    test=SinglyLinkedStack()
    test.push(10)
    test.push(20)
    test.push(30)
    test.push(40)
    test.pop()

class LinkedQueue(SinglyLinkedBase):
    #here we have to remove the tail sentinel
    def enqueue(self,e):
        if self.is_empty():
            newtail=self._insert_after(e,self._head)
        else:
            newtail=self._insert_after(e,self._tail)
        self._tail=newtail
        return newtail

    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty!")
        return self._delete_after(self._head,self._head._next)
    def first(self):
        return self._head._next._element

    #_____________________________________________________________________#
    # Creativity c-7.26
    def concatenate(self,Q):
        if not isinstance(Q,type(self)):
            raise ValueError("Wrong Type Input!")
        self._tail._next=Q._head._next
        self._tail=Q._tail
        self._size += len(Q)
        Q=None
        return self
if __name__=='__main__':
    a=LinkedQueue()
    for i in range(10):
        a.enqueue(i)
    b=LinkedQueue()
    for i in 'abcd':
        b.enqueue(i)
    c=a.concatenate(b)
    len(c)
    c.dequeue()



if __name__=='__main__':
    test=LinkedQueue()
    for i in range(10):
        test.enqueue(i)
    for i in range(10):
        test.dequeue()


class CircularQueue:

    class _Node:
        __slots__='_element','_next'

        def __init__(self,element,next):
            self._element= element
            self._next=next

    def __init__(self):
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0
    # use the sentinel here, to keep the tail as sentienl
    # but we cannot do this, because:
    # for a singlyLinked list, we cannot add a node to position previous to the tail

    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty!")
        oldhead=self._tail._next
        if self._size==0:
            self._tail=None
        else:
            self._tail._next=oldhead._next
        self._size -=1
        return oldhead._element

    def enqueue(self,e):
        new=self._Node(e,None)
        if self.is_empty():
            self._tail=new
            new._next=new
        else:
            new._next=self._tail._next
            self._tail._next=new
            self._tail=new
        self._size +=1

    def rotate(self):
        if self._size >0:
            self._tail=self._tail._next









