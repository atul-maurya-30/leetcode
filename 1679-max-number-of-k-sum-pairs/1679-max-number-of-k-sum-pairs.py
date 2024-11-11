class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        #it slightly uses the concept of two sums problem
        c=0
        seen={} #making hashmap
        for num in nums:
            t=k-num #to find second element

            #checking for the condtion
            if t in seen and seen[t]>0 : #if second element in seen and also if second element in seen have a value greater than 0
                c+=1 #increase the counter
                seen[t]-=1 #and also decrease the counter of that second element in seen
            else:
                if num in seen: #if present then incraese by 1
                    seen[num]+=1 
                else: #else give a value to 1
                    seen[num]=1
        return c #return the counter
