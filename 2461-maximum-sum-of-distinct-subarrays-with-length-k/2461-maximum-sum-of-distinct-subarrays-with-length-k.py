
#The sliding window + Defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
#       _______________
        n=len(nums)   #|
        if n<k:       #|-->> BASE CASE  
            return 0  #|
#       _______________|

        h=defaultdict(int) #USING DEFAULTDICT
        m=0 #MAX_SUM
        l=0 #LEFT
        w=0 #WINDOW SUM


#ADDING ELEMENT IN DICT
     #    RIGHT
     #      ↓  
        for r in range(n):  #OUR RIGHT INDEX IS MOVING FORWARD AS BY 1 ALWAYS
            w+=nums[r]  #IT IS USED FOR CALCULATING THE SUM OF SLIDING WINDOW
            h[nums[r]]+=1 #ADD ELEMENT IN DICT AND INCREASE IT COUNTS

#SLIDING WINDOW SIZE CHECKING
            if r-l+1>k: #WHEN SLIDING WINDOW SIZE EXCEEDS
                h[nums[l]]-=1
                if h[nums[l]]==0:
                    h.pop(nums[l]) #REMOVE THE ELEMENT FROM FRONT
                w-=nums[l] #AS NOW WE HAVE TO SUBTRACT THE VALUE OF DISCARDED ELEMENT
                l+=1 #LETS SHIFT THE SLDING WINDOW FORWARD
             
#CHECK FOR DISTINCT ELEMENTS(EXACTLY K ELEMENTS)             
            if r-l+1==k: #IF LENGTH OF SLIDING WINODW IS EQUALS TO K 
                if len(h)==k: 
                    m=max(m,w) #FIND THE MAX VALUE
        return m 

#HOPE THIS EXPLAINATION HELPS