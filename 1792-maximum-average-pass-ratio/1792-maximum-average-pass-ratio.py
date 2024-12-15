class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        r=len(classes)
        a=[]
        for i in range(r):
            o=classes[i][0]/classes[i][1]
            a.append(o)
        while extraStudents!=0:
            up_a=[]
            for i in range(r):
                new_o=(classes[i][0]+1)/(classes[i][1]+1)
                up_a.append(new_o)
        
            # it takes o(n)
            # best=0
            # best_delta=0.0
            # for i in range(r):
            #     delta=up_a[i]-a[i]
            #     if delta>best_delta:
            #         best_delta=delta
            #         best=i
            

#so we use max heap
            
            heap=[]
            for i in range(r):
                delta=up_a[i]-a[i]
                heapq.heappush(heap,(-delta,i)) #push negative delta for max heap
            _,best=heapq.heappop(heap)
            a[best]=up_a[best]
            classes[best][0]+=1
            classes[best][1]+=1
            extraStudents-=1
        k=0
        for i in range(r):
            k+=a[i]
        return k/r