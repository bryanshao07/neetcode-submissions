class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> vals = new HashSet<>();
        for (int num : nums){
            if (vals.contains(num)){
                return true;
            }
            vals.add(num);
        }
        return false;
        
    }
}