class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> h1 = new HashMap<>();
        HashMap<Character, Integer> h2 = new HashMap<>();
        char[] c1 = s.toCharArray();
        char[] c2 = t.toCharArray();
        for (char c : c1){
            if (h1.containsKey(c) == false){
                h1.put(c, 1);
            }
            else{
                h1.put(c, h1.get(c)+1);
            }
        }

        for (char c : c2){
            if (h2.containsKey(c) == false){
                h2.put(c, 1);
            }
            else{
                h2.put(c, h2.get(c)+1);
            }
        }

        return h1.equals(h2);
    }
}
