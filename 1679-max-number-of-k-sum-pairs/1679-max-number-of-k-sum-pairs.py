class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0
        seen={}
        for num in nums:
            t=k-num
            if t in seen and seen[t]>0 :
                c+=1
                seen[t]-=1
            else:
                if num in seen:
                    seen[num]+=1
                else:
                    seen[num]=1
        return c
