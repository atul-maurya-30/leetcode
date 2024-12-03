class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m=[]
        l=0
        for i in range(len(s)):
            if l<len(spaces) and i==spaces[l]:
                m.append(" ")
                l+=1
            m.append(s[i])
        return "".join(m)
