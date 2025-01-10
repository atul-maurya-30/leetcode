class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #hash table which is used to count the characters in words2 
        h=defaultdict(int)
        for i in words2:
            for j in i:
                h[j]=max(h[j],i.count(j))

        #list for storing the words        
        a=[]
        for i in words1:
            #make a hash map for each and every words1
            k=defaultdict(int)
            for j in i:
                k[j]=i.count(j)

            #now compare the words in hash table of words1 with the hash table of words2
            if all(k[j]>=h[j] for j in h):
                #if true for every value then append it
                a.append(i)
        return a


                
            


