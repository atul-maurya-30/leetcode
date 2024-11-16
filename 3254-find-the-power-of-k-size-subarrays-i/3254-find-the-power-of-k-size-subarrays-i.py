from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # n=len(nums)
        # m=[]
        # l=0
        # r=k
        # while r<n+1:
        #     j=nums[l:r]
        #     if j==sorted(j) and all(j[i]+1==j[i+1] for i in range(len(j)-1)):
        #         m.append(max(j))
        #     else:
        #         m.append(-1)
        #     l+=1
        #     r+=1
        # return m                

        # while r<=n:
        #     if nums[l:r]==sorted(nums[l:r]) and all(nums[i]+1==nums[i+1] for i in range(l,r-1)):
        #         m.append(max(nums[l:r]))
        #     else:
        #         m.append(-1)
        #     l+=1
        #     r+=1
        # return m

#above all are variants of sliding window
#and below are the code for deque  which is very efficient for using sliding window technique for this problem
     
        a=deque() #queue
        res=[-1]*len(nums) #initialised array with -1

        for i in range(len(nums)):
            # if queue is empty or last element is consecutive to current element
            if not a or a[-1]==nums[i]-1:
                a.append(nums[i])
                if len(a)>k:
                    a.popleft() #pop from left to maintain size
            else:
                a.clear() #clear the queue if sequence is broken
                a.append(nums[i]) #add the current no.
            if len(a)==k:
                res[i]=a[-1]
        return res[k-1:] #as our res length is same as the nums so we have to manage that portiion also

