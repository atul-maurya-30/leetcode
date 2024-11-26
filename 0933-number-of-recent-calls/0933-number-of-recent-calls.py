import collections
class RecentCounter:

    def __init__(self):
        #initialize a deque to store timestamps of recent requests
        self.dq=collections.deque()

    def ping(self, t: int) -> int:
        #add the current request timestamp to the deque
        self.dq.append(t)

        #remove timestamps that are outside the range(t-3000,t)
        while self.dq[0]<t-3000:
            self.dq.popleft() #remove the oldest timestamp from the range
        #return the count of timestamps within the valid range
        return len(self.dq) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)