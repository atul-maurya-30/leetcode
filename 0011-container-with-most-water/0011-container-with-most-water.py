class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m=0
        o=0
        j=len(height)-1

        
        while o<j:
            w=j-o
            a=min(height[o],height[j])*(w)
            m=max(m,a)

            if height[o]<height[j]:
                o+=1
            else:
                j-=1
        return m