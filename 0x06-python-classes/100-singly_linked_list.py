#!/usr/bin/python3
"""Write a class that defines a node of a singly linked list"""


class Node:
    """Define a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize data and next_node"""
        self.__data = data

        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve data"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a singly linked list"""

    def __init__(self):
        """Initialize head"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct
        sorted position in the list"""

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (
                    current.next_node is not None
                    and current.next_node.data < value
                    ):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Change the linked list into a string to be printed"""

        string = ""
        current = self.__head
        while current is not None:
            if current.next_node is None:
                string += str(current.data)
            else:
                string += str(current.data) + "\n"
            current = current.next_node

        return string
