class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ret = new int[k];
        Map<Integer, Integer> vals = new HashMap<>();
        for (int i : nums){
            vals.putIfAbsent(i, 0);
            vals.put(i, vals.get(i)+1);
            
        }
        List <int[]> bucket = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : vals.entrySet()){
            bucket.add(new int [] {entry.getValue(), entry.getKey()});
        }
        bucket.sort((a,b) -> b[0]-a[0]);

        for (int i = 0; i<k; i++){
            ret[i] = bucket.get(i)[1];
        }
        return ret;
    }
}
