class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1: ]:

            #discard previous sum if negative as it wont help us anywasy
            #+ add current num = keep current sum
            
            current_sum = max(current_sum, 0) + num 
            
            #update max sum
            max_sum = max(max_sum, current_sum)

        return max_sum
             