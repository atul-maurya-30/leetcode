class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            s=max(gifts)
            i=gifts.index(s)
            gifts[i]=int(s**0.5)
        return sum(gifts)
