class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for r in box:
            e=len(r)-1
            for c in range(len(r)-1,-1,-1):
                if r[c]=="#":
                    r[c],r[e]=".","#"
                    e-=1
                elif r[c]=="*":
                    e=c-1
        rot=[list(r) for r in zip(*box[::-1])]
        return rot