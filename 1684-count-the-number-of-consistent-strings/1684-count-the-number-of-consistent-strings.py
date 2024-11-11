class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        # for i in words:
        #     if all(char in allowed_set for char in i):
        #         c+=1
        # return c

        return sum(set(i).issubset(allowed_set) for i in words)