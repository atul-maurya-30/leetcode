class Solution:
    def removeStars(self, s: str) -> str:
        f=[]
        for i in s:
            if i!="*":
                f.append(i)
            else:
                f.pop()
        return "".join(f)

                