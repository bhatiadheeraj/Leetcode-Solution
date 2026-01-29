class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            res.append((point, self.calDistance(point[0],point[1])))
        partial = sorted(res, key = lambda point: point[1])[:k]
        cleanRes = []
        print(partial, sorted(res))
        for item in partial:
            cleanRes.append(item[0])
        return cleanRes
    def calDistance(self,x,y):
        return math.dist((0,0), (x,y))