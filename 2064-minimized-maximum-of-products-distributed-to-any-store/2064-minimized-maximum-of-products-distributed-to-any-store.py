class Solution:

    '''this function is used as for checking the limit of max items per person to mid'''
    def poss(self,mid,quantities,n):

        # check for each quantities of each product by using mid that it fulfil the store limit or not
        s=0
        for i in quantities:
            s+= (i+(mid-1))//mid #for adding the ciel value it is the alternative approach
            if s>n: #agar total stores jo hai wo jyada ho jaye available se to true kardo 
                return True # aur iska matlb ye hai ki current value jyada bada hai , aur hum distribute nhi kar skte hai
       
        return s>n #aur agar required stores kam ho jaye ya barabar ho jaye to false kardo

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1 #start value of pointer
        r=max(quantities) #set r for max value of quantities as for final value of pointer
        
        #use binary search
        while(l<r):
            #calculate mid value, that if store getting more items or not,if yes then increase lower bound by mid+1
            mid=(l+r)//2
            if self.poss(mid,quantities,n):
                l=mid+1

            #if not then just give the mid value to upper bound
            else:
                r=mid

        #at the end l is the maximized maximum no. of items per store 
        return l