# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arlist = nums1 + nums2
        arlist = sorted(arlist)
        length = len(arlist)
        if(length%2 !=0):
            return arlist[int(length/2)]
        else:
            index = int(length/2) 
            num1 = arlist[index]
            num2 = arlist[index-1]
            return (num1 + num2)/2
            
