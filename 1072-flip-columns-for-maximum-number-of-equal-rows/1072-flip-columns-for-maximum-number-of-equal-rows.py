class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m=0
        for i in range(len(matrix)):
            r=0
            for j in range(len(matrix)):
                if matrix[i]==matrix[j] or matrix[i]==[1-bit for bit in matrix[j]]:
                    r+=1
            m=max(m,r)
        return m