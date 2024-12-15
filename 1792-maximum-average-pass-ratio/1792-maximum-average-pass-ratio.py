class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        r=len(classes)
        heap=[]

        #calculate delta function to reduce the redundancy of code
        def cal(c):
            p,t=c
            delta=((p+1)/(t+1))-(p/t) #find delta value
            return delta
        
        #intialize heap with delta for each classes
        for i in range(r):
            heapq.heappush(heap,(-cal(classes[i]),i)) #max heap by negative index

        #distribute extra students to every classes
        while extraStudents>0:
            _,ind=heapq.heappop(heap) #get classes with maximum delta
            classes[ind][0]+=1 #add a student
            classes[ind][1]+=1 #update total class

            #recalculate the delta
            c=(classes[ind][0],classes[ind][1])
            heapq.heappush(heap,(-cal(c),ind))
            extraStudents-=1

        #calculate the final average ratio
        return sum(p/t for p,t in classes)/r
        
            

# time limit exceeded
#         r=len(classes)
#         a=[]
#         for i in range(r):
#             o=classes[i][0]/classes[i][1]
#             a.append(o)
#         while extraStudents!=0:
#             up_a=[]
#             for i in range(r):
#                 new_o=(classes[i][0]+1)/(classes[i][1]+1)
#                 up_a.append(new_o)
        
#             # it takes o(n)
#             # best=0
#             # best_delta=0.0
#             # for i in range(r):
#             #     delta=up_a[i]-a[i]
#             #     if delta>best_delta:
#             #         best_delta=delta
#             #         best=i
            

# #so we use max heap
            
#             heap=[]
#             for i in range(r):
#                 delta=up_a[i]-a[i]
#                 heapq.heappush(heap,(-delta,i)) #push negative delta for max heap
#             _,best=heapq.heappop(heap)
#             a[best]=up_a[best]
#             classes[best][0]+=1
#             classes[best][1]+=1
#             extraStudents-=1
#         k=0
#         for i in range(r):
#             k+=a[i]
#         return k/r