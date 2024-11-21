class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#step-1 #create a 2D null matrix  m*n
        null_matrix=[[0]*n for _ in range(m)]

        #0=empty, 1=Guarded, 2=wall/guard

#step:2 #marks all the guards and walls as 2
        for g in guards + walls:
            null_matrix[g[0]][g[1]]=2
        
#step:3 #use directional search
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        #process each guard
        for r,c in guards: #r,c are the positions of the guards
            # for understanding the concept of directions
            #refer to question no. 999 (https://leetcode.com/submissions/detail/1459079064/)
            for dr,dc in directions:

                nr,nc=r,c  #start from the guard postions

#step:4  Move in the current directions until a wall,gaurd or a boundary hits
                while True: 
                    #move one step in the current directions
                    nr+=dr
                    nc+=dc

#step:5             Stop if we hit boundary then break the loop
                    if  not(0<=nr<m and 0<=nc<n):
                        break
#step:6             #stop if we hit the wall or guard then also break loop
                    if null_matrix[nr][nc]==2:
                        break

#step:7             mark the current position as 1
                    null_matrix[nr][nc]=1

#step:8 Count all the number 0 (unguarded cells) in null_matrix
        u=0
        for r in null_matrix:
            u+=r.count(0)
        
#Step:9 Final step to return the sum of all the unguarded cells
        return u