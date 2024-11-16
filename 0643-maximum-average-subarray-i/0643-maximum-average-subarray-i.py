# from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # a=deque()
        # s=0
        # max_av=float('-inf')

        # for i in range(len(nums)):
        #     a.append(nums[i])
        #     s+=nums[i]

        #     if len(a)>k:
        #         s-=a.popleft()
            
        #     if len(a)==k:
        #         max_av=max(max_av,s/k)
        # return max_av

        s=sum(nums[:k])
        max_av=s/k

        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            max_av=max(max_av,s/k)
        return max_av