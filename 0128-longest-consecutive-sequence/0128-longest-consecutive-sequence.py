class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set(nums)
        sorted_s=sorted(s)

        n=len(sorted_s)
        i=0
        c=1 #initialize counter
        res=1 #assume minimu lenght of cosnecutive sequence is 1

        while i<n-1: #iterate for finding longest subsequence
            if sorted_s[i+1]==sorted_s[i]+1: #check for subsequence
                c+=1 #count
            else:
                c=1 #seqeunce broke
            i+=1 #increment i
            res=max(res,c) #largest subsequence
        return res        #return result



