class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = sorted(nums)
        
        for x in range(1,len(nums)):
            print(x)
            if num[x] == num[x-1] : return True

        return False
                
        
