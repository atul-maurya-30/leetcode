class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=set()
        c=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for row in r:
            for col in range(len(matrix[0])):
                matrix[row][col]=0
        for col in c:
            for row in range(len(matrix)):
                matrix[row][col]=0


            
                
