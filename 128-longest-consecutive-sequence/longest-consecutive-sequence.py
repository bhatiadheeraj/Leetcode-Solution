class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0

        for n in numset:
            if (n-1) not in numset: #the number that will be at begining of a sequence will have n-1 will not be part of nums
                length = 1
                while(n+length) in numset:
                    length +=1
                
                longest = max(length, longest)
        return longest

        