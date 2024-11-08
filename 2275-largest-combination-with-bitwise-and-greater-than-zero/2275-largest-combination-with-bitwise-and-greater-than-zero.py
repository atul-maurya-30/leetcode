class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        m=0  #store maximum count of 1 in any bit position
        b=0  #it is a counter go from 0 to 23
        while b<23:
            b_bit=0 # counts that how many 1 in the b-th positon
            for a in candidates: #now for checking the elements in the candidates

                #a>>b shifts the bits of a to the right by b positons
                b_bit+=(a>>b &1) #using &1 checks for bth pos is 1 not and after that it is add in b_bit by +1
            m=max(m,b_bit) #it is for checking which bit positon have maximum largest combination
            b+=1 #checking for next bit by incrementaion
        return m #maximum largest combination