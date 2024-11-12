class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        m=[]
        c=0

        for p,b in items:
            c=max(c,b)
            m.append((p,c))

        r=[]
        for q in queries:
            m_b=0
            for p,b in m:
                if p<=q:
                    m_b=b
                else:
                    break
            r.append(m_b)
        return r