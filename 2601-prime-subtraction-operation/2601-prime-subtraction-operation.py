class Solution(object):
    def isprime(self,limit):
        is_prime=[True]*(limit+1)
        i=2
        while i*i<=limit:
            if is_prime[i]:
                for j in range(i*i,limit+1,i):
                    is_prime[j]=False
            i+=1
        primes=[p for p in range(2,limit+1) if is_prime[p]]
        return primes
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m=max(nums)
        p=self.isprime(m)

        n=len(nums)
        prev=0
        for i in range(n):
            curr=nums[i]
            for j in reversed(p):
                if j<curr and curr-j>prev:
                    curr-=j
                    break    
            if curr<=prev:
                return False
            prev=curr
        return True