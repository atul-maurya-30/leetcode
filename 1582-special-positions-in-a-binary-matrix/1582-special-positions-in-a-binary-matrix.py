class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        row=[0]*m
        column=[0]*n
        special=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row[i]+=1
                    column[j]+=1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row[i]==1 and column[j]==1:
                    special+=1
        return special
                    