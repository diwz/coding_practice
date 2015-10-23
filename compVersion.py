class Solution1(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        lenv1, lenv2 = len(v1), len(v2)
        if lenv1 != lenv2:
            diff = abs(lenv1-lenv2)
            if lenv1 < lenv2:
                v1 += [0]*diff
            else:
                v2 += [0]*diff

        for i in range(max(lenv1, lenv2)):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0


class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        len1, len2 = len(v1), len(v2)
        lenMax = max(len1, len2)

        for i in range(lenMax):
            v1Token = v2Token = 0
            if i < len1:
                v1Token = int(v1[i])
            if i < len2:
                v2Token = int(v2[i])
            if v1Token < v2Token:
                return -1
            elif v1Token > v2Token:
                return 1
        return 0
