class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        a=[] #for list 
        g=-1 #for group tracker
        for i in range(len(groups)): #iteration through groups
            if groups[i]!=g: #check for change in group
                g=groups[i] #update the last group
                a.append(words[i]) #add word to res
        return a #return the result