class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        v={'a','e','i','o','u'}
        w=0
        max_v=0
        l=0
        for r in range(n):
            if s[r] in v:
                w+=1

            #if the window size exceeds then k then shrink the window
            if r-l+1>k:
                if s[l] in v:
                    w-=1
                l+=1
                
            #when exactly equal to k then it means it is last window
            if r-l+1==k:
                max_v=max(max_v,w)
        return max_v