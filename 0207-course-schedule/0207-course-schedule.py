class Solution:
    def dfs(self,g,u,visited):
        visited[u]=None #mark as visiting
        for v in g[u]:
            if visited[v] is None: #cycle found
                return True
            if visited[v] is False:
                if self.dfs(g,v,visited): #here v becomes curr and u becomes parent node
                    return True
        visited[u]=True
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)] #initialize adjacency list
        for u,v in prerequisites: #build graph from prerequisites
            g[u].append(v)
        visited=[False]*numCourses #initialized all nodes as unvisited
        for i in range(numCourses):
            if self.dfs(g,i,visited):  #cycle found
                return False
        return True