class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s=[]
        intervals.sort() #sort the interval in order
        for i in range(1,len(intervals)): 
            a=intervals[i-1][1] #start
            b=intervals[i][0]   #final
            if a>=b: #if final of current is less than or equAL to start of first 
                intervals[i]=[intervals[i-1][0],max(intervals[i-1][1],intervals[i][1])] #update the current element
            else:
                s.append(intervals[i-1]) #add the previous element
        s.append(intervals[-1]) #and atlast add the current element
        return s #return the new list of intervals