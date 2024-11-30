from node import Node
def comp_1(node_1, node_2):
    if node_1._capacity == node_2._capacity:
        return (node_1._bin_id - node_2._bin_id)
    else:
        return (node_1._capacity - node_2._capacity)
        
def comp_2(node_1, node_2):
    return (node_1._object_id - node_2._object_id)
    
def comp_3(node_1, node_2):
    return (node_1._bin_id - node_2._bin_id) 

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.compare_function = compare_function
    def height(self, node):
        if not node:
            return 0
        else:
            return node._height

    def is_balanced(self, node):
        return abs(self.height(node._leftchild) - self.height(node._rightchild)) <= 1

    def recompute_height(self, node):
        if node:
            x = 1
            if node._leftchild:
                x = node._leftchild._height +1
            if node._rightchild:
                x = max(x, node._rightchild._height + 1)
            node._height = x
    def left_left (self,node):
        temp = node._leftchild
        node._leftchild = temp._rightchild
        if temp._rightchild:
            temp._rightchild._parent = node
        temp._rightchild = node
        temp._parent = node._parent
        node._parent = temp
        if temp._parent and self.compare_function(temp._parent._element, node._element)>0:
            temp._parent._leftchild = temp
        elif temp._parent:
            temp._parent._rightchild = temp
        node = temp
        self.recompute_height(node._leftchild)
        self.recompute_height(node._rightchild)
        self.recompute_height(node)
        self.recompute_height(node._parent)
        return node
        
    def right_right(self,node):
        temp = node._rightchild
        node._rightchild = temp._leftchild
        if temp._leftchild:
            temp._leftchild._parent = node
        temp._leftchild = node
        temp._parent = node._parent
        node._parent = temp
        if temp._parent and self.compare_function(temp._parent._element, node._element)>0:
            temp._parent._leftchild = temp
        elif temp._parent:
            temp._parent._rightchild = temp
        node = temp
        self.recompute_height(node._leftchild)
        self.recompute_height(node._rightchild)
        self.recompute_height(node)
        self.recompute_height(node._parent)
        return node
    
    def left_right(self, node):
        node._leftchild = self.right_right(node._leftchild)
        return self.left_left(node)


    def right_left(self, node):
        node._rightchild = self.left_left(node._rightchild)
        return self.right_right(node)
    
    def balance(self,node):
        height1 = 0
        height2 = 0
        if node._leftchild:
            height1 = node._leftchild._height
        if node._rightchild:
            height2 = node._rightchild._height
        if (height1 - height2) == 2 or (height2 - height1)==2 :
            if height1 < height2:
                right_height1 = 0
                right_height2 = 0
                if node._rightchild._rightchild:
                    right_height2 = node._rightchild._rightchild._height
                if node._rightchild._leftchild:
                    right_height1 = node._rightchild._leftchild._height
                if right_height1 > right_height2:
                    node = self.right_left(node)
                else:
                    node = self.right_right(node)
            else:
                left_height1 = 0
                left_height2 = 0
                if node._leftchild._rightchild:
                    left_height2 = node._leftchild._rightchild._height
                if node._leftchild._leftchild:
                    left_height1 = node._leftchild._leftchild._height
                if left_height1 > left_height2:
                    node = self.left_left(node)
                else:
                    node = self.left_right(node)
        return node

    def insert(self,node, parent, element):
        if node is None:
            node = Node(element, parent)
        elif self.compare_function(node._element, element)>0:
            node._leftchild = self.insert(node._leftchild, node, element)
            height1 = 0
            height2 = 0
            if node._leftchild:
                height1 = node._leftchild._height
            if node._rightchild:
                height2 = node._rightchild._height
            if (height1 - height2) == 2 or (height2 - height1) == 2:
                if node._leftchild and self.compare_function(node._leftchild._element, element)>0:
                    node = self.left_left(node)
                else:
                    node = self.left_right(node)
        elif self.compare_function(element, node._element)>0:
            node._rightchild = self.insert(node._rightchild, node, element)
            height1 = 0
            height2 = 0
            if node._leftchild:
                height1 = node._leftchild._height
            if node._rightchild:
                height2 = node._rightchild._height
            if (height1 - height2) == 2 or (height2 - height1)==2:
                if node._rightchild and self.compare_function(node._rightchild._element, element)>0:
                    node = self.right_left(node)
                else:
                    node = self.right_right(node)
        self.recompute_height(node)
        return node
    def delete(self,node, element):
        if node:
            if node._element == element:
                if node._rightchild is None and node._leftchild is not None:
                    if node._parent:
                        if self.compare_function(node._element,node._parent._element)>0:
                            node._parent._rightchild = node._leftchild
                        else:
                            node._parent._leftchild = node._leftchild
                        self.recompute_height(node._parent)
                    node._leftchild._parent = node._parent
                    node._leftchild = self.balance(node._leftchild)
                    return node._leftchild
                elif node._leftchild is None and node._rightchild is not None:
                    if node._parent:
                        if self.compare_function(node._element, node._parent._element)>0:
                            node._parent._rightchild = node._rightchild
                        else:
                            node._parent._leftchild = node._rightchild
                        self.recompute_height(node._parent)
                    node._rightchild._parent = node._parent
                    node._rightchild = self.balance(node._rightchild)
                    return node._rightchild
                elif node._leftchild is None and node._rightchild is None:
                    if node._parent:
                        if self.compare_function(node._element, node._parent._element)>0:
                            node._parent._rightchild = None
                        else:
                            node._parent._leftchild = None
                        self.recompute_height(node._parent)
                    node = None
                    return None
                else:
                    temp = node
                    temp = temp._rightchild
                    while temp._leftchild:
                        temp = temp._leftchild
                    val = temp._element
                    node._rightchild = self.delete(node._rightchild, temp._element)
                    node._element = val
                    node = self.balance(node)
            elif self.compare_function(element, node._element)>0:
                node._rightchild = self.delete(node._rightchild, element)
                node = self.balance(node)
                
            elif self.compare_function(element, node._element)<0:
                node._leftchild = self.delete(node._leftchild, element)
                node = self.balance(node)
            self.recompute_height(node)
        return node    
    
    def min_value(self, root):
        p = root
        while p._leftchild is not None:
            p = p._leftchild
        return p

    def subtree_search(self, root, value):
        if root is None:
            return None
        elif self.compare_function(value, root._element)>0:
            if root._rightchild is not None:
                return self.subtree_search(root._rightchild, value)
        elif self.compare_function(root._element, value)>0:
            if root._leftchild is not None:
                return self.subtree_search(root._leftchild, value)
        return root

    def add(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self.root = self.insert(self.root,None, element)

    


    def remove(self, element):
        
        self.root = self.delete(self.root, element)
        
        
    def replace(self, before, after):
        node = self.subtree_search(self.root, before)
        if node is None:
            self.add(after)
        else:
            node._element = after
        self.balance(node)
        
    def greater_than(self, node, element):
        if self.root is None:
            return None
        else:
            p = self.subtree_search(node, element)
            if self.compare_function(element, p._element) >0:
                p = self.after(p)
            return p
   
    def last_position(self, node):
        while node._rightchild is not none:
            node = node._rightchild
        return node
    
    def after(self, node):
        if node._rightchild is not None:
            return self.min_value(node._rightchild)
        else:
            walk = node
            above = walk._parent
            while above is not None and walk== above._rightchild:
                walk = above
                above = walk._parent
            if above is None:
                return node
        return above
    
    def before(self, node):
        if node._leftchild is not None:
            return self.max_value(node._leftchild)
        else:
            walk = node
            above = walk._parent
            while above is not None and walk== above._leftchild:
                walk = above
                above = walk._parent
            if above is None:
                return node
        return above
    
    def max_value(self,root):
        p = root
        while p._rightchild is not None:
            p = p._rightchild
        return p
    
    def inorder_traversal(self, root):
        result = []
    
        if root is not None:
            result = result + self.inorder_traversal(root._leftchild)
        
            result.append(root._element._object_id)
        
            result = result + self.inorder_traversal(root._rightchild)
    
        return result
        
    def inorder_traversals(self, root):
        result = []
    
        if root is not None:
            result = result+ self.inorder_traversals(root._leftchild)
        
            result.append(root._element._capacity)
        
            result = result + self.inorder_traversals(root._rightchild)
    
        return result

        
    def smaller_than(self, node, element):
        if self.root is None:
            return None
        else:
            p = self.subtree_search(node, element)
            if self.compare_function(element, p._element) <0:
                p = self.before(p)
            return p