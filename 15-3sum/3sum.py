class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)

        for index in range(len(nums) - 2):
            i = nums[index]
            low = index + 1 
            high = len(nums) - 1
            
            while low < high:
                sum_of_all = i + nums[low] + nums[high]
                if sum_of_all == 0:
                    ret.add((i , nums[low] , nums[high]))
                    low +=1
                    high -=1
                elif sum_of_all < 0:
                    low +=1
                else:
                    high -=1
        return list(ret)

