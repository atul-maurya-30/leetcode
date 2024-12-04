class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       #we use tow deque approach here 
        rq=deque()
        dq=deque()
        #appending values of "R" and "D" in their respective queues
        for i in range(len(senate)):
            if senate[i]=="R":
                rq.append(i)
            else:
                dq.append(i)

        #loop end till queue is empty
        while dq and rq:
            x=rq.popleft()
            y=dq.popleft()
            if x<y: #if small index bans other senator 
                rq.append(x+len(senate)) #small index value should be append to its queue again
            else:
                dq.append(y+len(senate)) #else viceversa
        return "Radiant" if len(rq)>len(dq) else "Dire" #return the values by if-else