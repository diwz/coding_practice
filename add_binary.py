# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""
        a_idx = len(a) - 1
        b_idx = len(b) - 1

        while a_idx >= 0 or b_idx >= 0:
            a_digit = int(a[a_idx]) if a_idx >= 0 else 0
            b_digit = int(b[b_idx]) if b_idx >= 0 else 0
            val = (a_digit + b_digit + carry) % 2
            carry = (a_digit + b_digit + carry) // 2
            res = str(val) + res
            a_idx -= 1
            b_idx -= 1
        if carry == 1:
            res = str(carry) + res
        return res


class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""
        if len(a) < len(b):
            a, b = b, a

        a = "0" + a
        for i in range(0, (len(a) - len(b))):
            b = "0" + b

        for i in range(len(a)-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            carry = temp // 2
            res = str(temp % 2) + res

        if res[0] == "0":
            return res[1:]
        else:
            return res


class Solution3(object):
    def addBinary(self, a, b):
        bna = int(a, 2)
        bnb = int(b, 2)
        sum = bna + bnb
        return str("{0:b}".format(sum))

if __name__ == '__main__':
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    print(sol1.addBinary("101", "1"))
    print(sol2.addBinary("101", "1"))
    print(sol3.addBinary("101", "1"))
