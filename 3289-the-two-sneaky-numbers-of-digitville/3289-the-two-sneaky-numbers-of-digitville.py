class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m={}
        s=[]

        for num in nums:
            if num in m:
                m[num]+=1
            else:
                m[num]=1
        for num,c in m.items():
            if c>1:
                s.append(num)
        return s