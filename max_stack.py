# Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMax() -- Retrieve the maximum element in the stack.


class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.max) == 0 or x >= self.max[-1]:
            self.max.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.stack.pop()
        if top == self.max[-1]:
            self.max.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMax(self):
        """
        :rtype: int
        """
        return self.max[-1]
