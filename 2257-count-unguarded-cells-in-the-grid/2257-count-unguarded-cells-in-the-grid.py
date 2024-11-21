class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #create a 2D null matrix  
        null_matrix=[[0]*n for _ in range(m)]

        #0=empty, 1=Guarded, 2=wall/guard

        #marks all the guards and walls as 2
        for g in guards + walls:
            null_matrix[g[0]][g[1]]=2
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        for r,c in guards:
            for dr,dc in directions:
                nr,nc=r,c
                while True:
                    nr+=dr
                    nc+=dc
                    #stop if we hit boundary
                    if  nr<0 or nr>=m or n<=nc or nc<0:
                        break
                    #stop if we hit the wall or guard
                    if null_matrix[nr][nc]==2:
                        break
                    null_matrix[nr][nc]=1

        u=0
        for r in null_matrix:
            u+=r.count(0)
        return 0