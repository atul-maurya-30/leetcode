class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        m=[]
        c=0

        for p,b in items:
            c=max(c,b)
            m.append((p,c))


        def binary(query:int) ->int:
            l,r=0,len(m)-1
            d=0

            while l<=r:
                mid=(l+r)//2
                p,b=m[mid]
                if p<=query:
                    d=b
                    l=mid+1
                else:
                    r=mid-1
            return d

        r=[]
        for q in queries:
            r.append(binary(q))
        return r