class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # a=[]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         a.append(nums1[i]^nums2[j])
        # c=0
        # for i in range(len(a)):
        #     c^=a[i]
        # return c

        #since here brute force is not work
        #so we have to use the concept of properties of xor for the even or odd if the identities is same
        x1=0
        x2=0

        for i in range(len(nums1)): #store the values of xor of nums1 in x1
            x1^=nums1[i]
        for i in range(len(nums2)): #store the values of xor of nums2 in x2
            x2^=nums2[i]
                
        res=0
        if len(nums2)%2==1: #if length of nums2 is odd then take a xor of x1
            res^=x1 
        if len(nums1)%2==1: #if length of nums1 is odd then take a xor of x2
            res^=x2
        return res #return result