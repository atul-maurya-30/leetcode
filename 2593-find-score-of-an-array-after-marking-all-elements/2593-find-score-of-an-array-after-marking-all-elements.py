class Solution:
    def findScore(self, nums: List[int]) -> int:
        s=0 #Initialize score
        heap=[(num,i) for i,num in enumerate(nums)] #create a list of tuples (num,index) 
        heapify(heap) #convert it into min heap
        marked=[False]*len(nums) #to keep track of marked indices
        while heap:
            num,i=heappop(heap) #pop element with the smallest no.
            if not marked[i]: #if the index has not been visited yet
                s+=num # add into score

                #mark current ,left and right index visited
                if i-1>=0:
                    marked[i-1]=True #left
                    
                marked[i]=True       #current

                if i+1<len(nums):
                    marked[i+1]=True #right
        return s




        
        # n=len(nums)
        # #created a sorted ordered pair set of (value,index) pairs from nums
        # k=[(nums[i],i) for i in range(n)]
        # k.sort()
        # s=0 #score=0
        # visit=[False]*n
        # for v,i in k: #loop
        #     if visit[i]:
        #         continue
        #     s+=v #add value to score
        #     visit[i]=True

        #     #check and marked if the left neighbourif exists in set
        #     if i-1>=0 and not visit[i-1]: 
        #         visit[i-1]=True

        #     #check and marked if the right neighbour exists in set
        #     if i+1<n and not visit[i+1]:
        #         visit[i+1]=True

        # return s #return the score