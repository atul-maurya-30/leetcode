class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        #it slightly uses the concept of two sums problem
        c=0
        seen={} #making hashmap
        for num in nums:
            t=k-num #to find second element
            if t in seen and seen[t]>0 : #checking for the condition
                c+=1
                seen[t]-=1
            else:
                if num in seen:
                    seen[num]+=1
                else:
                    seen[num]=1
        return c
