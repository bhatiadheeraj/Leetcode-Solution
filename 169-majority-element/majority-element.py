class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_tracker = {}
        for item in nums:
            if counter_tracker.get(item,0) == 0:
                counter_tracker[item] = 1
            else:
                counter_tracker[item] += 1
        
        maxCount = 0
        num = 0
        threshold = math.floor(len(nums)/2)
        print(counter_tracker, threshold)
        for key,val in counter_tracker.items():
            if val >= threshold and val > maxCount:
                num = key
                maxCount = val
        return num
