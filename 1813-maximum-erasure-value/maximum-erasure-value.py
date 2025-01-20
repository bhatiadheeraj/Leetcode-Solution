class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # elements must be unique in subarray
        # score = sum 
        # max_score of subarray should be returned

        max_sum = 0
        i = 0 #i
        sum = 0
        seen = set()
        for j in range(len(nums)): # j
            while nums[j] in seen:
                seen.remove(nums[i])
                sum -= nums[i]
                i +=1 
            
            seen.add(nums[j])
            sum += nums[j]

            max_sum = max(max_sum,sum)
        return max_sum
        