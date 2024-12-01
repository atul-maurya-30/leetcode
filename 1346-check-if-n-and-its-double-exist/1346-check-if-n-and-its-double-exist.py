class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h={}
        for i in arr:
            if i*2 in h or (i%2==0 and i//2 in h):
                return True
            h[i]=None
        return False
                