from classes.node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.__head = None

    def add(self, data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            self.__head.next = self.__head
            self.__head.prev = self.__head
        else:
            # find the last node
            current_node = self.__head
            while current_node.next != self.__head:
                current_node = current_node.next
            
            # insert new node as next node of current last node
            current_node.next = new_node

            # set previous node of new node to current last node
            new_node.prev = current_node

            # set next node of new node to head node
            new_node.next = self.__head

            # set previous node of head node to new node
            self.__head.prev = new_node

    @property
    def head(self):
        return self.__head