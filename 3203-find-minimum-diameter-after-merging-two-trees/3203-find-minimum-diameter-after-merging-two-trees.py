class Solution:
    def bfs(self,adj,u):
        n=max(adj.keys())+1 #for size of graph
        visit=[False]*n #to track visited nodes
        q=deque([u]) #initiate the queue with start node u
        visit[u]=True #mark true for the start node
        d=0 #to store distance of the farthest node
        farthest_node=u #initially farthest node is the the start node

        # bfs loop
        while q: #until empty
            for _ in range(len(q)): #explore all nodes at current level
                node=q.popleft() #pop node from front
                farthest_node=node #update farthest node to the current

                #explore all neighbours of current node
                for i in adj.get(node,[]): #get nodes , default to empty list
                    if not visit[i]: #if neighbour is not visited
                        visit[i]=True #mark it visited
                        q.append(i) #append neighbour in the queue
            if q: #if more nodes to visit, increase distance
                d+=1
        #return farthest node and its distance
        return [farthest_node,d]
            
    def find_diameter(self,adj):
        #step-1 find farthest node from a random node in a tree

        farthest_node=self.bfs(adj,0)

        # step-2 farthest node we got above is nothing but one end of the diameter
        #step-3 Find the farthest node from the node we got above, that will be the other end of diameter i.e. diameter
        farthest_node=self.bfs(adj,farthest_node[0])
        return farthest_node[1] #diameter
    
    def make_adj(self,e): #create an adjacency list
        adj=defaultdict(list)
        for u,v in e:
            adj[u].append(v)
            adj[v].append(u) #bidirectional nodes
        return adj
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        #create adjacency list
        adj1=self.make_adj(edges1)
        adj2=self.make_adj(edges2)

        #now find diameters of tree1 and tree2
        d1=self.find_diameter(adj1)
        d2=self.find_diameter(adj2)
     
        #to find the value of minimum diameter
        combo=(d1+1)//2 + (d2+1)//2+1

        # return the maximum diameter between two trees or the new combo one
        return max(d1,d2,combo)