class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        a=[]
        n=len(word)
        i=0

        while i<n:
            j=i+1 #new index start for count
            while j<n and word[j]==word[i]:
                j+=1
            k=j-i
            while k>0:
                x=min(9,k)
                a.append(str(x))
                a.append(word[i])
                k-=x
            i=j
        return "".join(a)