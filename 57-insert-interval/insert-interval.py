class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        intervals = sorted(intervals)
        res = [intervals[0]]

        for start,end in intervals[1:]:
            if res[-1][1] < start:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res