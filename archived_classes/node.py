class Node:
    def __init__(self, data):
        self.__data = data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @next.setter
    def next(self, next_node):
        self._next = next_node

    @prev.setter
    def prev(self, prev_node):
        self._prev = prev_node
        