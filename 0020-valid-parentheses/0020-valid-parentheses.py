class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        p={
            "(":")","[":"]","{":"}"
        }
        for i in s:
            if i in p:
                stack.append(i)
            elif len(stack)==0 or i!=p[stack.pop()]:
                return False
        return len(stack)==0