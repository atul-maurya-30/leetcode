class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        max_o=0 #to store the max length
        w=0 #to track no. of zeros in current window
        l=0 #left pointer
        for r in range(n): #iteration start with right pointer 
            if nums[r]==0: #if the current element 0, increase the count
                w+=1
            
            #if no. of zero exceeds k,shrink the window from the left to right
            while w>k:
                if nums[l]==0:
                    w-=1
                l+=1
            max_o=max(max_o,r-l+1)
        return max_o