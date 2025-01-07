class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        b=set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]!=words[j]:
                    if words[j] in words[i]:
                        b.add(words[j])
        return list(b)
