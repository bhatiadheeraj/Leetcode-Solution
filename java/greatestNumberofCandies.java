/* https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/ */
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        /*n kids => 3 kids
        candies[] = [2,3,4]
        extraCandies = 19

        output : 
            result = [n]
            result[i] to be true/false such that candies[i] + ExtraCandies > greates 
        */
        
        int greatest = 0;
        for (int i=0; i<candies.length; i++) {
            if(candies[i] > greatest) greatest = candies[i];
        }
        ArrayList<Boolean> result = new ArrayList<>();
        for(int i=0; i<candies.length; i++) {
            if(candies[i] + extraCandies >= greatest) {
                result.add(true);
            }else {
                result.add(false);
            } 
        }
        return result;
    }
}
