class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=["1"]
        for i in range(2,n+1):
            if i%3==0 and i%5==0:
                s.append("FizzBuzz")
            elif i%3==0:
                s.append("Fizz")
            elif i%5==0:
                s.append("Buzz")
            else:
                s.append(str(i))
        return s