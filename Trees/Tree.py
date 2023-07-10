class Tree:

    class Position:
        def element(self):
            raise NotImplementedError("Can only be implemented by Subclass")
        
        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by SubClass")
        
        def __ne__(self, other):
            return not (self == other)
    
    def root(self, position):
        raise NotImplementedError("Must be implemented by SubClass")
    
    def parent(self, p):
        raise NotImplementedError("Must be implemented by Subclass")
    
    def num_children(self, p):
        raise NotImplementedError("Must be implemented by Subclass")
    
    def children(self, p):
        raise NotImplementedError("Must be implemented by Subclass")
    
    def __len__(self):
        raise NotImplementedError("Must be implemented by Subclass")
    
    def  is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, position):
        if self.is_root(position):
            return 0
        else:
            return self.depth(self.parent()) + 1
        
