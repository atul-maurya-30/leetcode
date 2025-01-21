class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        firstrow_sum=sum(grid[0])
        secondrow_sum=0
        min_robot2_sum=float(inf)

        for i in range(len(grid[0])):
            #robot1 took this strategy
            firstrow_sum-=grid[0][i]

            #robot2 will try to do best after robot1 has taken the above strategy
            best=max(firstrow_sum,secondrow_sum)
            min_robot2_sum=min(min_robot2_sum,best)
            secondrow_sum+=grid[1][i]
        return min_robot2_sum