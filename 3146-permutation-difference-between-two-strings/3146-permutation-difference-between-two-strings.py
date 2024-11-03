class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return sum(abs(i-s.index(t[i])) for i in range(len(t)))


        