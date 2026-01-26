class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # print(self.distanceToOrigin(1,-1))
        point_distance = {}
        point_distance_tuples = []
        for index in range(0, len(points)):
            point_distance[self.distanceToOrigin(points[index][0], points[index][1])] = points[index]
            point_distance_tuples.append((points[index], self.distanceToOrigin(points[index][0], points[index][1])))

        ret = sorted(point_distance_tuples, key = lambda x: x[1])
        count = 0
        res = []
        for item in ret:
            if count < k:
                res.append(item[0])
                count +=1
        return res

    def distanceToOrigin(self, x, y):
        # distance = (0-x)^2 + (0-y)^2
        # return sqrt(abs(distance))
        return math.dist([0,0],[x,y])