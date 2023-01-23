#!/usr/bin/python3
""" Testing """
class Node:
    """
    Node class
    """
    def __init__(self, data, next_node=None):
        """
        Initializes object with the data and sets next to None.
        next will be assigned later when new data needs to be added.
        """
        self.data = data
        self.next = next_node

    def get_data(self):
        """ Returns data """
        return self.data

    def get_next(self):
        """ Gets next node """
        return self.next

    def set_data(self, newdata):
        """ Sets current nodes data """
        self.data = newdata

    def set_next(self, newnext):
        """ Sets next node """
        self.next = newnext

class UnorderedList:
    """
    UnorderedList, single linked class
    """

    def __init__(self):
        """ Constructor of the FIFO Queue class """
        self.head = None

    def start(self):
        """ Returns start of the list """
        return self.head
        
    def is_empty(self):
        """ Returns True if the list is empty, False otherwise """
        return self.head is None

    def size(self):
        """ Returns the length of the list """
        no = 0
        if self.head is not None:
            no += 1
            next_item = self.head
            while next_item.next is not None:
                next_item = next_item.next
                no += 1
        return no

    def append(self, item):
        """ Append item last in the list """
        node = Node(item)
        if self.is_empty():
            self.head = node
        elif self.size() == 1:
            self.head.next = node
        else:
            # Find the last item, append the new node after
            next_item = self.head.next
            while next_item.next is not None:
                next_item = next_item.next
            next_item.next = node

    @staticmethod
    def print_x_last_elements(node, number):
        if node is None:
            return 0
        counter = ul.print_x_last_elements(node.get_next(), number)
        if counter < number:
            print(node.get_data())
        counter += 1
        return counter


ul = UnorderedList()
ul.append(1)
ul.append(2)
ul.append(3)
ul.append(4)
ul.append(7)

ul.print_x_last_elements(ul.start(), 3)
