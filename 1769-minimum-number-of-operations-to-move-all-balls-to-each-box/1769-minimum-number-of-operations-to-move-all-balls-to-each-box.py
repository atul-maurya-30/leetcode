class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[]
        a=[]
        for i in range(n):
            if boxes[i]=="1":
                a.append(i)
        for i in range(n):
            s=0
            for j in range(len(a)):
                s+=abs(a[j]-i)
            ans.append(s)
        return ans