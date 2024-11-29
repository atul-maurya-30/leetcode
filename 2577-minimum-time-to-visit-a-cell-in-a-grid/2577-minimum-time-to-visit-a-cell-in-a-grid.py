class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
# step:1base case
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
#step:2 initialization
        dir=[(0,1),(1,0),(-1,0),(0,-1)] #directions
        visited=[[False]*n for _ in range(m)] #visited matrix
        res=[[float('inf')]*n for _ in range(m)]
        #priority queue
        pq=[(grid[0][0],0,0)] #(time,row,col)

#step:3 Dijkstra like traversal
        while pq:#if its not empty
            t,r,c=heapq.heappop(pq) #pop with smallest values of time,row,col
            if r==m-1 and c==n-1: #if reach destination return time
                return t
            if visited[r][c]: #if visited then skip it
                continue
            visited[r][c]=True

            

#step:4 Exploring neighbours
            for i,j in dir:
                row,col=i+r,j+c
                #check for bounds and if not visited
                if not(0<=row<m and 0<=col<n and not visited[row][col]):
                    continue
                #calculate time needed to move cell(row,col)
                if t<grid[row][col]:#wait if the cell isnt yet accessible
                    w=grid[row][col]-t #timw neede to wait
                    next_t=grid[row][col]+(w%2)#adjust next time based on even/odd wait
                else:
                    next_t=t+1 #the cell is already accessible, we can move there in 1 step
                if next_t<res[row][col]:
                    res[row][col]=next_t
                    heapq.heappush(pq,(next_t,row,col))#push cell to heap with updated time
        return -1 #return -1 if reaching the bottom-right corner is not possible


