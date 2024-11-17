class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q=deque() #make a queue
        n=len(nums) #find the length
        q.append((0,-1))
        curr,ans=0,n+1

        for i in range(n):
            curr+=nums[i]
            while q and curr <=q[-1][0]:
                q.pop()
            
            while q and curr - q[0][0] >=k:
                _,j=q.popleft()
                ans=min(ans,i-j)

            q.append((curr,i))
        return ans if ans<=n else -1