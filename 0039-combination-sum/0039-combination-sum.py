class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def numbers(candidates,target,ans,temp,index):
            if target==0:
                ans.append(list(temp))
                return
            for i in range(index,len(candidates)):
                if target-candidates[i]>=0:
                    temp.append(candidates[i])
                    numbers(candidates,target-candidates[i],ans,temp,i)
                    temp.remove(candidates[i])
        ans=[]
        temp=[]
        arr=sorted(list(set(candidates)))
        numbers(arr,target,ans,temp,0)
        return ans