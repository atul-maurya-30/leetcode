class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        nums.append(0)
        m=[]
        l=0
        r=k
        while r<n+1:
            j=nums[l:r]
            if k==1:
                m.append(j[0])
            elif j==sorted(j) and all(j[i]+1==j[i+1] for i in range(len(j)-1)):
                a=max(j)
                m.append(a)
            else:
                m.append(-1)
            l+=1
            r+=1
        return m                

