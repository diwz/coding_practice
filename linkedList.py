class Node(object):
    """docstring for Node"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node, data):
        # Insert node right after existing node
        new_node = Node(data, node.next)
        node.next = new_node
        if self.tail is node:
            self.tail = new_node

    def insert_head(self, data):
        new_node = Node(data, None)
        self.head = new_node

    def insert_end(self, data):
        if self.tail is None:
            new_node = Node(data, None)
            self.head = self.tail = new_node
        else:
            self.insert(self.tail, data)

    def remove_after(self, node):
        node.next = node.next.next
        if node.next is None:
            self.tail = None

    def remove_head(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
