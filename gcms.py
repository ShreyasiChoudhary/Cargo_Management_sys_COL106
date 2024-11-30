from avl import AVLTree
from avl import comp_1
from avl import comp_2
from avl import comp_3
from object import Object
from object import Color
from bin import Bin

from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bins_capacity = AVLTree(comp_1)
        self.object_ids = AVLTree(comp_2)
        self.bin_ids = AVLTree(comp_3)


    def add_bin(self, bin_id, capacity):
        p = Bin(bin_id, capacity)
        self.bins_capacity.add(p)
        self.bin_ids.add(p)
            
        
    def add_object(self, object_id, size, color):
        object = Object(object_id, size, color)

        if color == Color.BLUE:
            dummy_bin = Bin(float('-inf'), object._size)
            bin_node = self.bins_capacity.greater_than(self.bins_capacity.root,dummy_bin)
            if bin_node is None or bin_node._element._capacity < object._size:
                raise NoBinFoundException()
            temp = bin_node._element
            self.bins_capacity.remove(bin_node._element)
            temp.add_object(object)
            self.bins_capacity.add(temp)
            self.object_ids.add(object)

    
        elif color == Color.YELLOW:  
            dummy_bin = Bin(float('-inf'), object._size)
            bin_node = self.bins_capacity.greater_than(self.bins_capacity.root,dummy_bin)
            if bin_node is None or bin_node._element._capacity < object._size:
                raise NoBinFoundException()
            capacity = bin_node._element._capacity
            dummy_bin = Bin(float('inf'), capacity)
            bin_node = self.bins_capacity.smaller_than(self.bins_capacity.root, dummy_bin)
            if bin_node is None or bin_node._element._capacity < object._size:
                raise NoBinFoundException()
            
            temp = bin_node._element
            self.bins_capacity.remove(bin_node._element)
            temp.add_object(object)
            self.bins_capacity.add(temp)
            self.object_ids.add(object)

        elif color == Color.RED: 
            max_bin_node = self.bins_capacity.max_value(self.bins_capacity.root)
            max_capacity = max_bin_node._element._capacity
            dummy_bin = Bin(float('-inf'), max_capacity)
            bin_node = self.bins_capacity.greater_than(self.bins_capacity.root, dummy_bin)
            if bin_node is None or bin_node._element._capacity < object._size:
                raise NoBinFoundException()
            temp = bin_node._element
            self.bins_capacity.remove(bin_node._element)
            temp.add_object(object)
            self.bins_capacity.add(temp)
            self.object_ids.add(object)

        elif color == Color.GREEN:  # For GREEN
            max_bin_node = self.bins_capacity.max_value(self.bins_capacity.root)
        
            if max_bin_node is None or max_bin_node._element._capacity < object._size:
                raise NoBinFoundException()
            temp = max_bin_node._element
            self.bins_capacity.remove(max_bin_node._element)
            temp.add_object(object)
            self.bins_capacity.add(temp)
            self.object_ids.add(object)

        else:
            raise NoBinFoundException()



    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        p = Object(object_id,0, Color.BLUE)
        q = self.object_ids.subtree_search(self.object_ids.root, p)
        if q._element._object_id == object_id:
            s = q._element._bin
            q._element._bin = None
            self.bins_capacity.remove(s)
            s.remove_object(object_id)
            self.bins_capacity.add(s)
            self.object_ids.remove(q._element)
        
        
    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        p = Bin(bin_id, 0)
        q=self.bin_ids.subtree_search(self.bin_ids.root, p)
        if q._element._bin_id == bin_id:
            s=q._element._capacity
            r=q._element.objects_tree.inorder_traversal(q._element.objects_tree.root)
            return (s,r)
        else:
            return None._element

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        p = Object(object_id, 0, Color.RED)
        q = self.object_ids.subtree_search(self.object_ids.root, p)
        if p._object_id == q._element._object_id:
            s = q._element._bin
            return s._bin_id
        else:
            return None._bin_id
        