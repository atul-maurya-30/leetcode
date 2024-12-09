class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        p=[0]*n #array to store prefix sum of alternating parity pairs
        r=[] #for storing bool values

        for i in range(1,n): #build prefix array
            if nums[i]%2!=nums[i-1]%2: #check if adjacent elements have different parity
                p[i]+=1 #increment if they have different parity
            p[i]+=p[i-1] #accumulate the value for prefix sum

        for u,v in queries:
            r.append(p[v]-p[u]==v-u) #true if all pairs are alternating
        return r

















#brute force approach but time limit exceeded so follow above approach
    # def isspecial(self,temp):
    #     for i in range(len(temp)-1):
    #         if not ((temp[i]%2==0 and temp[i+1]%2!=0) or (temp[i]%2!=0 and temp[i+1]%2==0)):
    #             return False
    #     return True 
    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     s=[]
    #     for u,v in queries:
    #         if u==v:
    #             s.append(True)
    #             continue
    #         sub=nums[u:v+1]
    #         if self.isspecial(nums[u:v+1]):
    #             s.append(True)
    #         else:
    #             s.append(False)
    #     return s