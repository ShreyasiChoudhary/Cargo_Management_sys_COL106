from avl import AVLTree
from avl import comp_1
from avl import comp_2
from avl import comp_3
from object import Object
from object import Color

class Bin:
    def __init__(self, bin_id, capacity):
        self._bin_id = bin_id
        self._capacity = capacity
        self.objects_tree = AVLTree(comp_2)
    

    def add_object(self, object):
        # Implement logic to add an object to this bin
        if self._capacity >= object._size:
            self._capacity = self._capacity - object._size
            object._bin = self
            self.objects_tree.add(object)

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        a = Object(object_id, 0, Color.RED)
        b = self.objects_tree.subtree_search(self.objects_tree.root, a)
        if b._element._object_id == object_id:
            c = b._element._size
            self._capacity = self._capacity + c
            self.objects_tree.remove(b._element)