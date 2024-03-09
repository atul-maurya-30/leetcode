class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""#empty String
        for i in zip(*strs):#use for itereating elements simultaneously
            if len(set(i))==1:#use for checking the same elements as if there is mulitple elements then its length is greater than 1
                a+=i[0]#append the value of a
            else:
                return a
        return a#return the value of a