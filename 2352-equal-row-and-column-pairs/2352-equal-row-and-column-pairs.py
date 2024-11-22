class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # #approach 1= Nested loop
        # n=len(grid)
        # c=0
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i]==[grid[k][j] for k in range(n)]:
        #             c+=1
        # return c



        #approach 2=  By hash map
        c=0 #counter
        h=defaultdict(int) #map

# Step:1 Store each row as a tuple in map        
        for i in grid:
            h[tuple(i)]+=1 #store row in map,using tuple for immutability,hashability and increment its frequency by 1
        
#step:2 For each column in grid, check that any row exists in map
        for j in range(len(grid[0])): #iterate through columns
            col=[] #to store current columns
            for i in range(len(grid)): #collect elements of the current column
                col.append(grid[i][j])
            
            c+=h[tuple(col)] #if the column matches in any row in the map , then increment the counter
        return c
