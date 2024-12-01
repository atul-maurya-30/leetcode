class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # h={}
        # for i in arr:
        #     if i*2 in h or (i%2==0 and i//2 in h):
        #         return True
        #     h[i]=None
        # return False
        
        f=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j:
                    if arr[i]==arr[j]*2 or (arr[i]%2==0 and arr[i]//2==arr[j]):
                        f=1
                        break
            if f==1:
                break
        return True if f==1 else False
                
        