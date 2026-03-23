class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for items in points:
            result.append((items,self.distance(items[0],items[1])))
        
        computed =  sorted(result, key= lambda res:res[1])[:k]
        result = []
        for item in computed:
            result.append(item[0])
        
        return result
    
    def distance(self,x,y):
        return math.dist([0,0],[x,y])