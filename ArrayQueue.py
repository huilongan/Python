'''
Here is a review on the queue
'''

#array-based queue
class Empty(Exception):
    pass

class ArrayQueue:
    DEFAULTCAPACITY=10

    def __init__(self):
        self._data=[None]*ArrayQueue.DEFAULTCAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty!")
        value=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self)
        self._size -=1
        return value

    def enqueue(self,e):
        if len(self)==ArrayQueue.DEFAULTCAPACITY:
            self._resize(2*ArrayQueue.DEFAULTCAPACITY)
        if self._size==0:
            self._data[self._front]=e
        else:
            avail=(self._front+len(self))%len(self)
            self._data[avail]=e
        self._size +=1

    def _resize(self,incre):
        old=self._data
        self._data=[None]*incre
        start=self._front
        for i in range(len(old)):
            self._data[i]=old[self._front]
            self._front=(self._front+1)%len(old)
        self._front=0


if __name__=="__main__":
    test=ArrayQueue()
    for i in range(10):
        test.enqueue(i)
    test.is_empty()
    for i in range(10):
        test.dequeue()
    test.is_empty()
    for i in range(20):
        test.enqueue(i)
    len(test)

