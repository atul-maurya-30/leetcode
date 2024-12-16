class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h=[(x,i) for i,x in enumerate(nums)]
        heapify(h)
        for _ in range(k):
            # m=min(nums)
            x,i=h[0]
            heapreplace(h,(x*multiplier,i))
        for x,i in h:
            nums[i]=x
        return nums