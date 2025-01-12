class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2!=0:
            return False
        open=[]
        openclose=[]
        for i in range(len(s)):
            if locked[i]=="0":
                openclose.append(s[i])
            elif s[i]=="(":
                open.append(s[i])
            elif s[i]==")":
                if open:
                    open.pop()
                elif openclose:
                    openclose.pop()
                else:
                    return False
        return len(open)<=len(openclose) and (len(open)+len(openclose))%2==0