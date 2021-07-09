#question :  https://leetcode.com/problems/third-maximum-number/submissions/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSorted = list(set(nums))
        numSorted = (sorted(numSorted, reverse=True))
        if len(numSorted) >= 3: return numSorted[2]
        return numSorted[0]
