class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=0
        m=0
        for i in gain:
            a=a+i
            m=max(a,m)
        return m