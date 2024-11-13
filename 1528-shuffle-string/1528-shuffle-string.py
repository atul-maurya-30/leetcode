class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        h=[""]*len(s)
        
        for i,ind in enumerate(indices):
            h[ind]=s[i]
        return "".join(h)