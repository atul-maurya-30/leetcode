class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in range(len(words)):
            if words[i].startswith(pref):
                c+=1
        return c