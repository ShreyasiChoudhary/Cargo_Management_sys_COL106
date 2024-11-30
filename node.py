
class Node:
    def __init__(self, element, parent = None):
        self._element = element
        self._parent = parent
        self._leftchild = None
        self._rightchild = None
        self._height = 1
        