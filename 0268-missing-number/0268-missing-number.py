class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        b=[]
        for i in range(0,l+1):
            b.append(i)
        for i in b:
            if i not in nums:
                return i
        return -1
            
                
                