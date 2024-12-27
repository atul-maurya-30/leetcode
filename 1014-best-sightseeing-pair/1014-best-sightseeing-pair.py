class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m=float("-inf")
        memo=set()
        for i in range(len(values)):
            for j in range(i,len(values)):
                if (i,j) in memo:
                    continue
                if i<j:
                    s=values[i] + values[j] + i - j
                    m=max(m,s)
                    memo.add((i,j))
        return m