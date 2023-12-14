class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        onerow=[0]*m
        onecol=[0]*n
        
        for i in range(m):
            for j in range(n):
                onerow[i]+=grid[i][j]
                onecol[j]+=grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j]=2*(onerow[i]+onecol[j])-m-n
        return grid