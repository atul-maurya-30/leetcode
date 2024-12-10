class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        #collect index of violeting index
        v=[]
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                v.append(i)
        res=[]

        #process each query
        for s,e in queries:
            s+=1
            f=False
            l=0
            r=len(v)-1

            #binary search to find if any index in "v" is in range of queries 
            while l<=r:
                mid=l+(r-l)//2
                if v[mid]<s:
                    l=mid+1
                elif v[mid]>e:
                    r=mid-1
                else:
                    f=True
                    break

            #if no violeting index is found, the subarray is special add into result
            res.append(not f)
        return res



















    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     n=len(nums)
    #     p=[0]*n #array to store prefix sum of alternating parity pairs
    #     r=[] #for storing bool values

    #     for i in range(1,n): #build prefix array
    #         if nums[i]%2!=nums[i-1]%2: #check if adjacent elements have different parity
    #             p[i]+=1 #increment if they have different parity
    #         p[i]+=p[i-1] #accumulate the value for prefix sum just like cummulative sum

    #     #process each query
    #     for u,v in queries:
    #         #check if no. of alternating pairs in subarray matches the no. of pairs
    #         r.append(p[v]-p[u]==v-u) #true if all pairs are alternating
    #     return r

















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