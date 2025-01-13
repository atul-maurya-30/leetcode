class Solution:
    def countBits(self, n: int) -> List[int]:
        m=[]
        for i in range(n+1):
            b=(bin(i)[2:])
            m.append(b.count("1"))
        return m