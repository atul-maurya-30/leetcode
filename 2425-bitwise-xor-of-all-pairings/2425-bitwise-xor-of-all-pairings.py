class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                a.append(nums1[i]^nums2[j])
        c=0
        for i in range(len(a)):
            c^=a[i]
        return c