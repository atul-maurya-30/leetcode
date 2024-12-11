class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s=[]
        intervals.sort()
        if len(intervals)==1:
            return intervals
        for i in range(1,len(intervals)):
            a=intervals[i-1][1]
            b=intervals[i][0]
            if a>=b:
                intervals[i]=[intervals[i-1][0],max(intervals[i-1][1],intervals[i][1])]
            else:
                s.append(intervals[i-1])
        s.append(intervals[-1])
        return s