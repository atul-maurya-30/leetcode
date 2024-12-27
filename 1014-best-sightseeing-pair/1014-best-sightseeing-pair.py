class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # #optimized code after brute force
        # # we can see that only j is changing so we can store the value of maximum values till current in a variable m


        # i=float("-inf") #for storing max value of values[i]+i
        # max_m=float("-inf") #used for storing the maximum score
        # for j in range(1,len(values)):
        #     k=values[j]-j #it gives the current score of values[j]
        #     l=values[j-1]+(j-1) #it gives the previous score of values[j-1] 
        #     i=max(i,l) #update max value for ith
        #     max_m=max(max_m,i+k) #update max value for the score
        # return max_m

        i=float("-inf") #for storing max value of values[i]+i
        max_m=float("-inf") #used for storing the maximum score
        heap=[]
        for j in range(1,len(values)):
            k=values[j]-j #it gives the current score of values[j]
            l=values[j-1]+(j-1) #it gives the previous score of values[j-1] 
            heapq.heappush(heap,-l)
            i=-heap[0]
            max_m=max(max_m,i+k) #update max value for the score
        return max_m