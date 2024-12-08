class Solution:
    #step-9 binary search to find the first event that starts after the given end time 
    def binary_for_finding_next_element(self,events,endt):
        l,r=0,len(events)-1 #initialise binary search bounds
        ans=len(events) #default to no valid next found

        while l<=r: #binary search loop
            mid=l+(r-l)//2 #safe mid calculation

            if events[mid][0]>endt: #event starts after current event's 
                ans=mid #calculate for next event
                r=mid-1 #search for left
            else:
                l=mid+1 #search for right
        return ans #return next valid event's index

    #step-5 dp to calculate max value of up to 2 non-overlapping events
    def find(self,events,i,count,n,memo):
        if count==2 or i>=n: #stop if 2 events selected or no events left 
            return 0

        if memo[i][count]!=-1: #return result if already computed
            return memo[i][count]

        #step:6 find the index of the next valid event that starts after the current event ends
        nex=self.binary_for_finding_next_element(events,events[i][1]) #use binary search

        #step:7 option 1- take the current event and solve for the next valid event
        take=events[i][2]+self.find(events,nex,count+1,n,memo)

        #step:8 option 2- Take the current event and solve for the next valid event 
        not_take=self.find(events,i+1,count,n,memo)

        memo[i][count]=max(take,not_take)
        return memo[i][count] #return computed maximum value

#step:1 main function to solve problem
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #step-2 Sorting elements for perform binary search with ease
        events.sort()
        n=len(events)
#step:3 Dynamic programming used for store results and to avoid same subproblem multiple times
        dp=[[-1]*3 for _ in range(n)]

        #step-4 start solving from the first event with no events selected
        return self.find(events,0,0,n,dp)