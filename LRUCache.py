class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = DoubleLinkedList()
        self.map = dict()

    def get(self, key):
        """
        :rtype: int
        """
        if (key in self.map) and self.map[key]:
            self.cache.remove(self.map[key])
            self.cache.addHead(self.map[key])
            return self.map[key].val
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addHead(self.map[key])
            self.map[key].val = value
        else:
            node = Node(key, value)
            self.map[key] = node
            self.cache.addHead(node)
            if self.size == self.capacity:
                del self.map[self.cache.tail.key]
                self.cache.removeTail()
            else:
                self.size += 1

class Node(object):
    """docstring for Node"""
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    """docstring for DoubleLinkedList"""
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head is self.tail:
            self.head, self.tail = None, None
            return
        if node is self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node is self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeTail(self):
        self.remove(self.tail)

    def addHead(self, node):
        if self.head is None:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None
