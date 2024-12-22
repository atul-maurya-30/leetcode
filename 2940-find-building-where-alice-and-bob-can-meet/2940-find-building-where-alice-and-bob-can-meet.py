#deferred queries, that cannot be answered immediately and are postponed for later processing
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # we use concept of heap ds
        #initialise result with -1 for all queries
        res=[-1]*len(queries)
        q=[[] for _ in range(len(heights))]
    
        #now we process each query
        for i,(alice,bob) in enumerate(queries):
            if alice>bob: #for easy processing ensure alice always smaller than bob
                alice,bob=bob,alice
        
            #if alice and bob are same and alice are already shorter, then dont do anything just det result to bob
            if alice==bob or heights[alice]<heights[bob]: 
                res[i]=bob
            else:
                #other wise , defer the query for processing later when bob is comes
                q[bob].append((heights[alice],i))

        #min heap for processing deferred queries easily
        min_heap=[]

        #iterate through each buildings one by one
        for i,height in enumerate(heights):
            # add all deferred queries for current building into heap
            for def_q in q[i]:
                heappush(min_heap,def_q)

            #now process queries in heap
            #remove queries where building height is taller than or equal to the deferred height
            while min_heap and min_heap[0][0]<height:
                #extract query index from heap and set result into building index
                _,q_index=heappop(min_heap)
                res[q_index]=i

        return res #return final result