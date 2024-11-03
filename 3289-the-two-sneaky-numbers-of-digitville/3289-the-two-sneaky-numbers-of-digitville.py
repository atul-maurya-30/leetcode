class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m={} #dictionary to store count of each no.
        s=[] #list for storing the output

        for num in nums:
            if num in m: #check if no, is already in the dictionary
                m[num]+=1 #increment it by 1 if no. is found
            else:
                m[num]=1 # initialize the count to 1 if the no. is new
        for num,c in m.items(): #iterate through the m
            if c>1: #check if the count of the no. is greater than 1
                s.append(num) #if correct then add inton list
        return s #return the list