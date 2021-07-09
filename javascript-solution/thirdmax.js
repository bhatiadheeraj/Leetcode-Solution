/**
https://github.com/bhatiadheeraj/Leetcode-Solution.git

LeetCODE LINK : https://leetcode.com/problems/third-maximum-number/submissions/
**/

var thirdMax = function(nums) {
    let numsSorted = nums.sort((a,b) => b-a).filter((item, index) => nums.indexOf(item) === index);
    if(numsSorted.length >=3) return numsSorted[2];
    return numsSorted[0];
};
