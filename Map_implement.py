'''
Here I implement a LinkedList to separate chaining hash table
'''
class Empty(Exception):
    pass
from collections import MutableMapping

class MapBase(MutableMapping):

    class _Item:

        __slots__='_key','_value'

        def __init__(self,k,v):
            self._key=k
            self._value=v

        def __eq__(self, other):
            return type(self) is type(other) and self._key is other._key

        def __ne__(self, other):
            return not self==other

        def __lt__(self, other):
            return self._key < other._key


class SinglyLinkedList:

    class _Node:
        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next

    def __init__(self):
        self._head=self._Node(None,None)
        self._size = 0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0

    # BigO cost: O(n)
    def _locate(self,e):
        cursor=self._head
        while cursor._next is not None:
            if cursor._next._element==e:
                return (cursor,cursor._next)
            cursor = cursor._next
        raise ValueError("No such a value been found!")
    # BigO cost: O(1)
    def _add(self,e):
        new=self._Node(e,None)
        if self.is_empty():
            self._head._next=new
        else:
            new._next=self._head._next
            self._head._next=new
        self._size += 1

    # BigO cost: O(n)
    def _change(self,e,ne):
        try:
            pre,bid=self._locate(e)
            pre._element=ne
        except ValueError:
            print("Not such a value!")

    def _del(self,e):
        try:
            pre,bid=self._locate(e)
            pre._next=bid._next
            bid=None
            self._size -= 1
        except ValueError:
            print("Not such a value!")

    def __iter__(self):
        cursor=self._head._next
        if self.is_empty():
            raise Empty("The list is empty!")
        while cursor is not None:
            yield cursor._element
            cursor = cursor._next

from random import randrange
class ChainHashTable(MapBase):
    '''
    use _Item to store key and value pairs
    implement SinglyLinkedList into separate chaining
    '''


    def __init__(self,cap=11,p=109345121):
        self._table=[None]*cap
        self._scale=1+randrange(p-1)
        self._shift=randrange(p)
        self._size = 0
        self._prime=p

    def _hash_function(self,k):
        return (self._scale*hash(k)+self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._size


    def __setitem__(self, k, v):
        if self._size>len(self._table)//2:
            self._rehasing(len(self._table)*2-1)
        loc=self._hash_function(k)
        if self._table[loc] is None:
            self._table[loc] = SinglyLinkedList()
        if self._table[loc].is_empty():
            self._table[loc]._add(self._Item(k,v))
            self._size += 1
        else:
            found=False
            for item in self._table[loc]:
                if item._key == k:
                    item._value=v
                    found=True
            if not found:
                self._table[loc]._add(self._Item(k,v))
                self._size += 1



    def __getitem__(self, k):
        loc=self._hash_function(k)
        if self._table[loc] is None:
            raise KeyError("Key Error: "+ repr(loc))
        else:
            for item in self._table[loc]:
                if item._key==k:
                    return item._value

    def __delitem__(self, k):
        loc=self._hash_function(k)
        if self._table[loc] is None:
            raise KeyError("Key Error: "+ repr(loc))

        else:
            for item in self._table[loc]:
                if item._key==k:
                    self._table[loc]._del(item)
                    self._size -=1
                    return
            raise KeyError("Key Error: "+ repr(loc))

    def __iter__(self):
        if self._size >0 :
            for bucket in self._table:
                if bucket is not None and not bucket.is_empty():
                    for item in bucket:
                        yield item._key

    def _rehasing(self,c):
        old=list(self.items())## this attribute comes from ABC (MutableMapping)
        self._size = 0
        self._table=[None]*c
        for (k,v) in old:
            self.__setitem__(k,v) ## or self[k]=v

if __name__=='__main__':
    a=ChainHashTable()
    d={i:chr(i) for i in range(100)}
    for i in range(100):
        a[i]=d[i]
        len(a)
        list(a)
    for i in range(100):
        del a[i]
        len(a)
        list(a)