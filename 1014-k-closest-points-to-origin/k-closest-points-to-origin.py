class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for item in points:
            result.append((item, self.calc(item[0],item[1])))
        ret = sorted(result, key = lambda x:x[1])
        res = []
        for item in ret[:k]:
            res.append(item[0])
        return res
        
    def calc(self,x,y):
        return dist((0,0),(x,y))