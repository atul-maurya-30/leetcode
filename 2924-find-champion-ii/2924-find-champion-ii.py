class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
#step 1: create an array and store all the v part from edges in it 
        s=[0]*n #initialise idegree array for all nodes

        for row in edges: #iterate all edge
            s[row[1]]+=1 #increment by 1 in indegree

        c=0 #champion candidate 
        c_count=0 #champion count
# step:2 take a loop for checking that there is any champion exists(0) in the created array if found then save it and increase champion count by 1
        for i in range(n): #check nodes for indegree 0 
            if s[i]==0: #nodes with no incoming edges
                c_count+=1 #increment the count of champions
                c=i #store the champion

        return -1 if c_count>1 else c #return -1 if multiple champions
