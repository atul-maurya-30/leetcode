class Solution:
    #i=curr index of target;j=curr index of words; freq=For storing the frequency of all alphabets indexed wise; m=length of target; k=length of word in words
    def solve(self,i,j,freq,target,m,k,memo):
        mod=(10**9)+7 #given in problem for dealing with largest value

        #base cases
        if i==m:
            return 1 #only one way to form a target string
        if j==k:
            return 0 #no ways to form a target string

        #if already exist in memo then return
        if memo[i][j]!=-1:
            return memo[i][j]

        #if not taken then just recall for next upcoming word
        not_taken=self.solve(i,j+1,freq,target,m,k,memo)%mod

        #if taken then select word as well as multiply it by frequency for possible ways of forming string and move to next ALPHABET of target as well as next upcoming word
        taken=freq[ord(target[i])-ord("a")][j] * self.solve(i+1,j+1,freq,target,m,k,memo)%mod


        #store the sum of all ways for pick or skip in memo and also take mod
        memo[i][j]=(taken+not_taken)%mod
        return memo[i][j] #return total frequency

    def numWays(self, words: List[str], target: str) -> int:
        m=len(target)
        k=len(words[0])

        memo=[[-1]*k for _ in range(m)] #use for memoize

        freq=[[0]*k for _ in range(26)] #2d array use for storing the frequency of every alphabets in the words with respect to index
        for i in range(k):
            for w in words:
                char=w[i]
                freq[ord(char)-ord("a")][i]+=1 #counter for increasing count value

        return self.solve(0,0,freq,target,m,k,memo) #call for function and return answer