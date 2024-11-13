class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def counting(final):
            c=0
            l=0
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]<=final:
                    c+=(r-l)
                    l+=1
                else: r-=1
            return c
        return counting(upper)-counting(lower-1)