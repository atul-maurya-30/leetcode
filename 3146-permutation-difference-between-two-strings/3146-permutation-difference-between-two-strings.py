class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s)!=len(t):
            return -1
        n=len(s)
        m=0
        for i in range(n):
            for j in range(n):
                if s[i]==t[j]:
                    m+=(abs(i-j))
        return m


        