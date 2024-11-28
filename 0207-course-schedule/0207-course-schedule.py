class Solution:
    def dfs(self,g,u,visited):
        visited[u]=None
        for v in g[u]:
            if visited[v] is None:
                return True
            if visited[v] is False:
                if self.dfs(g,v,visited): #here v becomes curr and u becomes parent node
                    return True
        visited[u]=True
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            g[u].append(v)
        visited=[False]*numCourses
        for i in range(numCourses):
            if not visited[i] and self.dfs(g,i,visited):
                return False
        return True