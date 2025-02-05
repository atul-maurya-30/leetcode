class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        h=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                h.append(i)
        s2_l=list(s2)
        if len(h)==0:return True
        if len(h)==2:
            s2_l[h[0]],s2_l[h[1]]=s2_l[h[1]],s2_l[h[0]]
            return s1=="".join(s2_l)
        else:
            return False
        