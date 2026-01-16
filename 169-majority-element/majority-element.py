from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = floor(len(nums) // 2)
        dict_vals = Counter(nums)

        maxVal = -1
        ret = 0

        print(dict_vals, threshold)
        for key,val in dict_vals.items():
            if val >= threshold and val > maxVal:
                maxVal = val
                ret = key

        
        return ret 