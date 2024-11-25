class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                m[i][j]=max(
                    grid[i][j:j+3]+
                    grid[i+1][j:j+3]+
                    grid[i+2][j:j+3]
                )
        return m