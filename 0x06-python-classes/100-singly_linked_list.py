#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None:
            if not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")

        self.__next_node = value



class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        return self.print()

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            while(self.__head.next_node is not None):
                self.__head = self.__head.next_node

            self.__head.next_node = Node(value)

    def print(self):
        while(self.__head is not None):
            print(self.__head.data)
            self.__head = self.__head.next_node

        return ""

