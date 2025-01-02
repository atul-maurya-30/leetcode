class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #step1 to define the vowels
        vow={"a","e","i","o","u"}

        #step2 to intialize prefix sum array
        pre_sum=[0]*(len(words)+1)


        #step3 to compute prefix sum
        for i,word in enumerate(words):
            if word[0] in vow and word[-1] in vow :
                pre_sum[i+1]=pre_sum[i]+1
            else:
                pre_sum[i+1]=pre_sum[i]

        #step4 to resolve queries using prefix_sum
        res=[]
        for u,v in queries:
            c=pre_sum[v+1]-pre_sum[u]
            res.append(c)
            
        #step5 to return final result
        return res 







        # aloo=[]
        # vow={"a","e","i","o","u"}
        # for j in range(len(words)):
        #     a=words[j][0]
        #     b=words[j][-1]
        #     if a in vow and b in vow:
        #         aloo.append(words[j])
        # l=[]
        # for i in range(len(queries)):
        #     u,v=queries[i]
        #     c=0
        #     for j in range(u,v+1):
        #         if words[j] not in aloo:
        #             continue
        #         else:
        #             c+=1
        #     l.append(c)
        # return l