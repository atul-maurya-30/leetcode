class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=[]
        for i in s:
            if len(m)<2 or i != m[-1] or i!=m[-2]:
                m.append(i)
        return "".join(m)
            
        