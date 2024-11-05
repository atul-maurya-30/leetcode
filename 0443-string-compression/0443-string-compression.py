class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n=len(chars)
        if n==1:
            return 1
        i=0
        w=0
        while i<n:
            c=chars[i]
            count=0
            while i<n and chars[i]==c:
                count+=1
                i+=1
            
            chars[w]=c
            w+=1
            
            if count>1:
                for digit in str(count):
                    chars[w]=digit
                    w+=1
        return w