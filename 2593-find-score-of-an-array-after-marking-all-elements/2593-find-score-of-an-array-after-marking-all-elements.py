class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        #created a sorted ordered pair set of (value,index) pairs from nums
        k=[(nums[i],i) for i in range(n)]
        k.sort()
        s=0 #score=0
        visit=[False]*n
        for v,i in k: #loop
            if visit[i]:
                continue
            s+=v #add value to score
            visit[i]=True

            #check and marked if the left neighbourif exists in set
            if i-1>=0 and not visit[i-1]: 
                visit[i-1]=True

            #check and marked if the right neighbour exists in set
            if i+1<n and not visit[i+1]:
                visit[i+1]=True

        return s #return the score