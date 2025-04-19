class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        #if we sort this array then it will not affect the given problem
        nums.sort()

        # we make this function for overcoming the problem of redundancy of writing the given code
        def counting(final):
            c=0 #counter for counting elements
            l=0 #left pointer
            r=len(nums)-1 #right pointer
            while l<r: #loop start
                if nums[l]+nums[r]<=final: #for checking the conditon of given problem as
                                            # it is given that lower<=nums+nums[j]<=upper

        #so we use a concept of line system as we want a range between upper and lower
                    c+=(r-l)  # we use this becuase we have to count the elements in the given range
                    l+=1 #after that we have to increment left pointer
                else: r-=1 #else we have to decrement rightb pointer
            return c #it will give the total counts of uppper and lower 
        
        #initialize the function counting 
        return counting(upper)-counting(lower-1) # as lower is also included in the condition so we use lower-1
        #and return the result