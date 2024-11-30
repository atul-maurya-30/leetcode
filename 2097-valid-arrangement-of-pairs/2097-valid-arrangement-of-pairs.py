class Solution:
    def dfs(self,adj,u,path):
        while adj[u]:
            v=adj[u].pop()
            self.dfs(adj,v,path)
        path.append(u)
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#step:1 Build the adjacency list and track in-degree and out-degree        
        adj=defaultdict(list)
        for u,v in pairs:
            adj[u].append(v)
        outdeg=defaultdict(int)
        indeg=defaultdict(int)
        for u,v in pairs:
            outdeg[u]+=1
            indeg[v]+=1

#step:2 Find the starting node(s)
        s=pair[0][0]
        for i in adj:
            if outdeg[i]-indeg[i]==1:
                s=i
                break

#step:3 Perform hierholzer's algorithm to find euler path 
        p=[]
        self.dfs(adj,s,p)
        p.reverse()
        k=[]
        for i in range(1,len(p)):
            k.append([p[i-1],p[i]])
        return k
