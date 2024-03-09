class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return a
            a+=first[i]
        return a