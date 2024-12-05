class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n=len(start)
        i,j=0,0 #two pointers of start and target

        #loop until we traverse the whole strings
        while i<n or j<n:
            #skip the underscores in both start and target
            while i<n and start[i]=="_":
                i+=1
            while j<n and target[j]=="_":
                j+=1

            #if both pointers reached the end, break
            if i==n or j==n: 
                return i==n and j==n
            if start[i]!=target[j]:
                return False
            #for "L", it can only move left, "R" can only move right
            if start[i]=="L" and i<j:
                return False
            if start[i]=="R" and i>j:
                return False
            i+=1
            j+=1
        return True
