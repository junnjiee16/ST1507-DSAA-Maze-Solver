from classes.node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)