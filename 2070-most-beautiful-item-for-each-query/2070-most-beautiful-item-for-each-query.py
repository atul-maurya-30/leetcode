class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #it is a straight forward problem as a easy level
        #sort the items by price
        items.sort()
        
        #compute new maximum beauty for each price
        m=[]
        c=0
        for p,b in items: #p= price
                          #b= beauty
            c=max(c,b)
            m.append((p,c))

        #binary search function for finding max beauty fir price<=query
        def binary(query:int) ->int:
            l,r=0,len(m)-1 #l=left ; r=right
            d=0 #default value if no item found

            while l<=r:
                mid=(l+r)//2 #for finding mid value

                #unpacking the data of m, which having max values of beauty 
                p,b=m[mid] #p=price ; b= beauty

                if p<=query: #check for prices which is less then queries
                    d=b #update default value to the beautyof the item
                    l=mid-1 
                else:
                    r=mid+1
            return d

        r=[]
        for q in queries:
            r.append(binary(q))
        return r