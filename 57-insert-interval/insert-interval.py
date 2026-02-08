class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        res = [intervals[0]]

        for start, end in intervals[1:]:
            print(start,end)
            if start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res