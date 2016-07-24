from TreeBase import Tree as Tree
class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        ## return an iteration of Positions representing p's children
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)