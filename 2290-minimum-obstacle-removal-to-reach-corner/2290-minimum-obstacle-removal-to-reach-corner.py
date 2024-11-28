class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])  #rows and columns
        #direction : right ,up,down,up
        dir=[(0,1),(1,0),(0,-1),(-1,0)] 

    #initialise the result grid with infinity (unreachable values) for all the cells
        res=[[inf]*n for _ in range(m)]
        res[0][0]=0 #starting point have 0 obstacles

        #priority queue (min_heap) to store curr cell and its obstacle count,with least obstacle count processed
        pq=[(0,0,0)] #(obstacles_count,x,y)

        while pq: #loop until priority queue is emptys
            d,i,j=heappop(pq) #pop cell with minimum obstacle count
            
            for dx,dy in dir: #explore all directions
                x,y=i+dx,j+dy #use for new coordinates

                if 0<=x<m and 0<=y<n: #check for upper and lower boundations
                    w=1 if grid[x][y]==1 else 0 #if there's an obstacle weight=1

                    if d+w<res[x][y]: #check if shorter path found
                        res[x][y]=d+w #update obstacle count
                        heappush(pq,(res[x][y],x,y)) #add new state into queue

        return res[m-1][n-1] #return minimum obstacle count for the bottom-right corner