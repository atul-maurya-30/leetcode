class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #Finding the rook
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":
                    r0,r1=i,j  #we finally find the position at this point

                
        t=0 #counter for counting that how many hits by rook to pawn

        #directional search
        #four directions are considered for rook i.e.
        #down =>[1,0] increase row by 1 i.e. it goes down
        #right=>[0,1] increase col by 1 i.e. it goes right
        #up   =>[-1,0]decrease row by 1 i.e. it goes up
        #left =>[0,-1]decrease col by 1 i.e. it goes left
        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            m,n=r0+i,r1+j #move one steps in the current direction
            while 0<=m<8 and 0<=n<8: #ensure the coordinates remain within the board
                if board[m][n]=="p":  #pawn found ,increament the count
                    t+=1 
                if board[m][n]!=".": #any other piece blocks leads to break the loop and block the path
                    break
                m,n=m+i,n+j #continue in the same direction
        return t #return the count