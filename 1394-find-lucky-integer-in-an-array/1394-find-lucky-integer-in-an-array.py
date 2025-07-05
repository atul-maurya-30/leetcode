class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        for num in sorted(c.keys(),reverse=True):
            if c[num]==num:
                return num
        return -1

