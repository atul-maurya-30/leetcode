class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        for i in range(0,len(gain)):
            m=a[i]+gain[i]
            a.append(m)
       
        return max(a)