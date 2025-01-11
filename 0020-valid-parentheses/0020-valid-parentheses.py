class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        for i in s:
            if i in "({[":
                x.append(i)
            else:
                if not x or (i==")" and x[-1]!="(") or (i=="}" and x[-1]!="{") or (i=="]" and x[-1]!="["):
                    return False
                x.pop()
        return not x
        
