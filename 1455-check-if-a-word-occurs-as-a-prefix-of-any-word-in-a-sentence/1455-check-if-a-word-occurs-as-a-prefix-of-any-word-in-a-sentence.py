class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=sentence.split()
        for i,code in enumerate(a):
            if code.startswith(searchWord):
                return i+1
            
        return -1


