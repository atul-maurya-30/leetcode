class Solution:
    def __init__(self):
        self.cost=[0,0,0] #ticket cost for 1,7 and 30- day passes
        self.memo=[] #Memoization array

    def solve(self,n,days):
        if n>=len(days): #base case: no more days to process
            return 0
        
        if self.memo[n]!=-1: #if already exist in memo then return
            return self.memo[n]

        #option1: buy 1 day pass
        take_one=self.cost[0]+self.solve(n+1,days)

        #option2: buy 7 day pass
        i=n
        while i<len(days) and days[i]<days[n]+7: #find first day beyond 7 days
            i+=1
        take_seven=self.cost[1]+self.solve(i,days) #if no days found take last day as updated ith value

        j=n
        while j<len(days) and days[j]<days[n]+30: #find first day beyond 30 days
            j+=1
        take_thirty=self.cost[2]+self.solve(j,days) #if no days found take last day as updated jth value

        #store result into memo
        self.memo[n]=min(take_one,take_seven,take_thirty) #minimum cost for current day
        return self.memo[n]
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.cost=costs #set ticket costs
        self.memo=[-1]*len(days) #initialize a memo
        return self.solve(0,days) #start from day 0



# same concept of question as below one
#https://leetcode.com/submissions/detail/1492630775/
