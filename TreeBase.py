class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            return not self == other

    def root(self):
        ##return the position of root of Tree
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        ##return the position of the parent of position p
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        ##return the number of children of position p
        raise NotImplementedError("Must be implemented by subclass")

    def children(self):
        ##generate an iteration of Positions representing p's children
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        ##return the size of the tree
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0