class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        m=[]
        l=0
        r=k
        # while r<n+1:
        #     j=nums[l:r]
        #     if j==sorted(j) and all(j[i]+1==j[i+1] for i in range(len(j)-1)):
        #         m.append(max(j))
        #     else:
        #         m.append(-1)
        #     l+=1
        #     r+=1
        # return m                


        while r<=n:
            if nums[l:r]==sorted(nums[l:r]) and all(nums[i]+1==nums[i+1] for i in range(l,r-1)):
                m.append(max(nums[l:r]))
            else:
                m.append(-1)
            l+=1
            r+=1
        return m

