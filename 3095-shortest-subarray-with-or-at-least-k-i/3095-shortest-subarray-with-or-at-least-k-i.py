class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        a=float('inf')
        n=len(nums)
        
        for i in range(0,n):
            s,l=0,0
            for j in range(i,n):
                s|=nums[j]
                l+=1
                if s>=k:
                    a=min(a,l)
        return -1 if a==float('inf') else a