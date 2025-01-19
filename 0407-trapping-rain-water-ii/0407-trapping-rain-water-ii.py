class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        #dimensions of the heightMap
        m,n=len(heightMap),len(heightMap[0])

        #directions for moving to negihboring cells(right,left,top,up)
        dir=[(0,1),(0,-1),(1,0),(-1,0)]

        #priority queue (min heap) to store bound
        bound=[]

        #2d list to track visited cells
        visit=[[False]*n for _ in range(m)]
        
        #add boundary cells to heap and mark them as visited
        for r in range(m):
            for c in (0,n-1): #leftmost and rightmost columns
                 heapq.heappush(bound,(heightMap[r][c],r,c))
                 visit[r][c]=True
                
        for c in range(n):
            for r in (0,m-1): #topmost and bottommost columns
                 heapq.heappush(bound,(heightMap[r][c],r,c))
                 visit[r][c]=True

        #visited to keep track of the total trapped water
        trap=0

        # process the cells in the priority queue
        while bound:
            #get the cell with the smallest height
            height,i,j=heapq.heappop(bound)

            #explore all fours neighboring cells
            for di,dj in dir:
                ni,nj=di+i,dj+j

                #checking if the neighboring celll is within bounds and not visited 
                if 0<=ni<m and 0<=nj<n and not visit[ni][nj]:
                    #compute trapped water in the neighboring cell
                    trap+=max(0,height-heightMap[ni][nj])

                    #add the neighboring cell to heap with its effective height
                    #the effective height is the maximum of the current height and the neighboring cell height
                    heapq.heappush(bound,(max(height,heightMap[ni][nj]),ni,nj))

                    #mark visited to neigboring cell
                    visit[ni][nj]=True

        #return the total trapped water
        return trap