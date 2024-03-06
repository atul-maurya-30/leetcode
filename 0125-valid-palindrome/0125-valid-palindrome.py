class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i.isalnum()==True:
                string+=i.lower()
        return string==string[::-1]
    
