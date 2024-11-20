class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)

       #first we count all the elements in string as per a,b,c.
        c_a=c_b=c_c=0
        for char in s:
            if char=="a":
                c_a+=1
            elif char=="b":
                c_b+=1
            elif char=="c":
                c_c+=1
        if (c_a<k or c_b<k or c_c<k):
            return -1  #not possible to del k characters so return -1

    #after counting all the elements we have to check for conditions.

    #initiate with the sliding window approach
        delete=0
        l=0 #left 
        r=0  #right
        while r<n:
            #we use window such that count of element is decreased by 1
            if s[r]=="a":
                c_a-=1
            elif s[r]=="b":
                c_b-=1
            else:
                c_c-=1

            #if deletion count of any char becomes less than k then just shrink the window
            #again increase count because we have to move forward for finding elements, that we have to delete
            while (l<=r) and (c_a<k or c_b<k or c_c<k):
                if s[l]=="a":
                    c_a+=1
                elif s[l]=="b":
                    c_b+=1
                else:
                    c_c+=1
                l+=1 #move left pointer forward
            delete=max(delete,r-l+1)
            r+=1 #also move right pointer forward

        #since we dont need count of delete so just subtract from 
        #the n then we will get our minimum number of minutes
        return n-delete 