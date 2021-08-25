/* Question https://leetcode.com/problems/concatenation-of-array/submissions/*/
class Solution {
    public int[] getConcatenation(int[] nums) {
        int length_ans = 2 * nums.length;
        int ans[] = new int[length_ans];
        for (int i =0; i < nums.length; i++) {
            ans[i] = nums[i];
            ans[i+nums.length] = nums[i];
        }
        return ans;
    }
}
