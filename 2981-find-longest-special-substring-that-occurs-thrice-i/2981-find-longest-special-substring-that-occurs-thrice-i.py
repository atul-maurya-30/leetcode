class Solution:
    def maximumLength(self, s: str) -> int:
        n=len(s)
        sub={}#dictionary to store the frequency of substrings
        for i in range(n):
            curr="" #initialize an empty substring
            for j in range(i,n):
                if not curr or curr[-1]==s[j]: #if characters are the same then extend the substring
                    curr+=s[j] 
                    sub[curr]=sub.get(curr,0)+1 #count the substring
                else:
                    break #stop if characters differ

        res=0 #variable to track the maximum length of a valid substring
        #check the frequency of each substring and find the longest one that appears at least 3 times
        for ss,c in sub.items():
            if c>=3 and len(ss)>res:
                res=len(ss)
        return -1 if res==0 else res