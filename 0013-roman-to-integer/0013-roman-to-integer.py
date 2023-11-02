class Solution:
    def romanToInt(self, s: str) -> int:
          #create a dictionary 
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        #let take n
        n = 0
        #if there is uncertain roman numerals come then replace it as per roman rule
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            n += romans[char]
        return n
        