class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not len(stack):
                    return False
                elif i == ']' and stack.pop() != '[':
                    return False
                elif i == '}' and stack.pop() != '{':
                    return False
                elif i == ')' and stack.pop() != '(':
                    return False
        return len(stack) == 0
