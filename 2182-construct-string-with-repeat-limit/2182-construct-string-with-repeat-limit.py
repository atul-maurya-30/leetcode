class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        #step-1 Count freq of charcters
        f={}
        for i in s:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1

        #step-2 Create a list of characters sorted in descending order
        sorted_s=[]
        for i,c in f.items():
            sorted_s.append([i,c])
        sorted_s.sort(reverse=True) #sort in descendig order

        #step-3 create a result string
        res=""
        j=0
        while j<len(sorted_s):
            i,c=sorted_s[j]
            if c<=repeatLimit:
                #add all occurences of current character
                res+=i*c
                j+=1
            else:
                #add up to repeatLimit occurences
                res+=i*repeatLimit
                sorted_s[j][1]-=repeatLimit #update remaining count

                
                #add the next largest character if available
                if j+1<len(sorted_s):
                    nex_i,nex_c=sorted_s[j+1]
                    res+=nex_i
                    sorted_s[j+1][1]-=1

                    #remove the next character if its count becomes 0
                    if sorted_s[j+1][1]==0:
                        sorted_s.pop(j+1)
                else:
                    #no characters left, to add then just break the loop
                    break
            
        return res