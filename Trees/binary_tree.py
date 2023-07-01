from Tree import Tree

class BinaryTree(Tree):
    def left(self, position):
        raise NotImplementedError("Must be implemented by subclass")
    
    def right(self, position):
        raise NotImplementedError("Must be implemented by subclass")
    
    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.left(position)
            
