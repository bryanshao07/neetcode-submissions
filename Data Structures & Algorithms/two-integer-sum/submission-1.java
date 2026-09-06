class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> vals = new HashMap<>();
        int[] ans = new int [2];
        for (int i = 0; i<nums.length; i++){
            if(vals.containsKey(target-nums[i])){
                ans[0] = vals.get(target-nums[i]);
                ans[1] = i;
            }
            else{
                vals.put(nums[i], i);
            }
        }
        return ans;
    }
}
