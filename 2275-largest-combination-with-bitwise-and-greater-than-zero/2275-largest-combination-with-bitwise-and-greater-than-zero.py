class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        m=0
        b=0
        while b<24:
            b_bit=0
            for a in candidates:
                b_bit+=(a>>b &1)
            m=max(m,b_bit)
            b+=1
        return m