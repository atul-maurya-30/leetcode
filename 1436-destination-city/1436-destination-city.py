class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        b=set()
        for i in paths:
            b.add(tuple(i[0]))
        for i in paths:
            if tuple(i[1]) not in b:
                return i[1]