class Solution:
    #we need helper function that count the value of maximum sum of subarrays
    def helper(self,i,c,s,k,memo):
        if c==0:                                    #|for count
            return 0                            
                                                    #| BASE CASE
        if i>=len(s):                               #|for overbound we got invalid value so for counter that part we have to give the minimum value for the helper function      
            return float("-inf") 

        #check if current index is already computed
        if (i,c) in memo:
            return memo[(i,c)]

        take=s[i]+self.helper(i+k,c-1,s,k,memo) #recall the function for taking the subarray with maximum value
        not_take=self.helper(i+1,c,s,k,memo) #recall function for skipping subarrays 

        #store result into memo
        memo[(i,c)]=max(take,not_take) #max value among take or not_take
        return  memo[(i,c)]#return max value

    #core part of the code
    def solve(self,s,c,i,k,res,memo): #s=subrray;c=3;i=current index;k=total subarray length;res:for storing the index of maximum subarrays
        if c==0:return #base case for count
        if i>=len(s):return #base case for overbound

        take=s[i]+self.helper(i+k,c-1,s,k,memo) #for picking current subarray
        not_take=self.helper(i+1,c,s,k,memo) #for skipping current subarray by indexing +1

        #for deciding whether to pick or skip array and store 0th index of subarray into res    
        if take>=not_take:
            res.append(i)
            #move forward to next subarray after selecting current
            self.solve(s,c-1,i+k,k,res,memo)
        else:
            #move forward if current subarray is not maximum
            self.solve(s,c,i+1,k,res,memo)

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        #we use sliding window approach for storing the value of subarrays sum according to the value of k
        sub=[]
        i,j=0,0
        w=0
        while j<len(nums):
            w+=nums[j]
            if j-i+1==k:
                sub.append(w)
                w-=nums[i]
                i+=1
            j+=1
        #intialise res for storing the 0th index of subarrays
        res=[]
        memo={} #initialize for memoization
        self.solve(sub,3,0,k,res,memo)
        return res