class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_VAL, MIN_VAL = 2147483647, -2147483648 
        str = str.strip()
        i,n = 0, len(str)

        sign = 1
        if i < n and (str[i] == '+'):
        	i += 1
        elif i< n and (str[i] == '-'):
        	i += 1
        	sign = -1

        num = 0
        upperbound = MAX_VAL // 10
        while i < n and str[i].isdigit():
        	digit = int(str[i])
        	if num > upperbound or (num == upperbound and digit >= 8):
        		return MAX_VAL if sign == 1 else MIN_VAL
        	num = num * 10 + digit
        	i += 1
        return num * sign