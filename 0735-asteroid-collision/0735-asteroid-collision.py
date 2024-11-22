class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[] #stack
        for i in asteroids:
            if i>0: #if postive then just add it into stack 
                s.append(i)
            else:
                while s and s[-1]>0 : # as 0 is the no. that is positive or negative so we dont want that also
                    m=s.pop()
                    if m==-i: #same size ,both explode
                        break
                    elif m>-i: #positive asteroid is bigger, so the left moving asteroid explodes
                        s.append(m)
                        break
                else:
                    s.append(i)
                        
        return s
                        