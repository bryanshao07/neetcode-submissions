class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> val = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int curr = target-nums[i];
            if (val.containsKey(curr)){
                return new int[] {val.get(curr), i};
            }
            else{
                val.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}
