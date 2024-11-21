class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h={}
        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        return len(h.values())==len(set(h.values()))