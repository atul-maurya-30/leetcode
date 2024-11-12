class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d={} #dictionary
        # m=0 #maximum count
        # c=0 #Max Count

        # for n in nums:
        #     d[n]=1+d.get(n,0)
        #     if d[n]>c:
        #         m=n
        #         c=d[n]
        # return m

        t=max(set(nums),key=lambda x:nums.count(x))
        return t