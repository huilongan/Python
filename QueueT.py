class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:

        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next

    def __init__(self):
        self._head=self._Node(None,None)
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0

    def top(self):
        return self._head._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty!")
        old=self._head._next
        self._head._next=old._next
        self._size -=1
        return old._element

    def enqueue(self,e):
        new=self._Node(e,None)
        if self.is_empty():
            self._head._next=new
        else:
            self._tail._next=new
        self._tail=new
        self._size +=1

if __name__=='__main__':
    test=LinkedQueue()
    for i in range(10):
        test.enqueue(i)
    test.top()
    len(test)
    test.is_empty()
    for i in range(10):
        test.dequeue()
    test.dequeue()
    test.is_empty()
    len(test)