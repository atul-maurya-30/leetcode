class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen: #checking for 2nd pair no.
                return ([seen[target-num],i])
            elif num not in seen:
                seen[num]=i #if not in the dictionary then add element to dictionary with index value i
        
                    
              