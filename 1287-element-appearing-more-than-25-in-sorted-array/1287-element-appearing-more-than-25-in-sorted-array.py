class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        l=n//4
        for i in range(n-l):
            if arr[i]==arr[i+l]:
                return arr[i]
        return -1