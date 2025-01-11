class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
# step:1 track rows and columns that needs to be zeros
        row=set()
        col=set()


#step:2 find the rows and columns containing zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)  #store value of rows
                    col.add(j)  #store value of columns

        for r in row: #set rows to zero
            for j in range(n):
                matrix[r][j]=0
        for c in col: #set cols to zero
            for i in range(m):
                matrix[i][c]=0
                
                    