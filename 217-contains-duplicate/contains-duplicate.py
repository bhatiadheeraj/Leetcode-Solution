class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}

        for item in nums:
            if num_count.get(item, 0) == 0 :
                num_count[item] = 1
            elif num_count.get(item) == 1:
                return True
        return False