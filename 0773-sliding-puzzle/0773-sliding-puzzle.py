class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        #mapping of possible directions of elements in the puzzle
        dir={
            0:[1,3], #0 postion can go to index 1 or 3
            1:[0,2,4], #1 position can go to index 0,2 or 4
            2:[1,5], #2 postion can go to index 1 or 5
            3:[0,4], #3 position can go to index 0 or 4
            4:[1,3,5], #4 position can go to index 1,3 or 5
            5:[2,4] #5 position can go to index 2 or 4
        }
        #flatten the 2d board into a single string
        s="".join([str(col) for row in board for col in row])

        #initialization of bfs queue
        #each element in the queue is a tuple
        #curr position of 0,board which already converted into string,number of moves for solving puzzle
        dq=deque([(s.index("0"),s,0)]) 

        #to initialize the set, to track of visited sets for avoiding revisiting and infinte loops  
        visit=set(s)

        #implement bfs to explore all possible states of puzzle board
        while dq:
            i,s,l=dq.popleft() #deque the curr state 

            # check that board is in solved state
            if s=="123450":
                return l #return no. of moves required for solving puzzle

            s_arr=list(s) #for easy manipulation convert string into list

            #explore all pssoble moves for the 0
            for j in dir[i]: #j is a valid index where 0 can move
                new_s_arr=s_arr.copy() #make a copy of current board

                #swap the 0 with the index j
                new_s_arr[i],new_s_arr[j]=s_arr[j],s_arr[i]

                #convert new board state back to the string
                new_s="".join(new_s_arr)

                #if new state not visited yet
                if new_s not in visit:

                    #add new state to the queue with updated index and increment count by 1
                    dq.append((j,new_s,l+1))

                    #mark new state as visited
                    visit.add(new_s)

        #if bfs complete without finding solution ,return -1
        return -1