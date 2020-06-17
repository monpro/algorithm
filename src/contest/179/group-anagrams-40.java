class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList();
        
        HashMap<Integer, List<String>> map = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        int[] primes = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101
        }; 

        for (String s : strs) {
            int score = score(s, primes);
            List<String> list = map.getOrDefault(score, new ArrayList<>());
            list.add(s);
            map.put(score, list);
        }
        res.addAll(map.values());
        return res;
    }
    
    private int score(String s, int[] primes) {
        int score = 1;
        for (char c : s.toCharArray()){
            score *= primes[c-'a'];
        }
        return score;
    }
}