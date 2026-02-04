class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if anytime current sum becomes zero we start from that subarray
        # notice we have to return sum not subarray

        maxSum = nums[0]
        currentSum = nums[0]
        
        for num in nums[1:]:
            currentSum = max(currentSum, 0) + num
            maxSum = max(maxSum, currentSum)
        
        return maxSum