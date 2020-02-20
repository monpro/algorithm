import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countArrangement(int N) {
        if(N == 0)
            return 0;
        
        int[] result = new int[1];
        int[] used = new int[N + 1];
        helper(N, 1, used, result);
        return result[0];
    }
    
    public void helper(int N, int pos, int[] used, int[] result){
        if(pos > N){
            result[0]++;
            return;
        }
        for(int i = 1; i <= N; i++){
            if(used[i] == 0 && (i % pos == 0 || pos % i == 0)){
                used[i] = 1;
                helper(N, pos + 1, used, result);
                used[i] = 0;
            }
        }
    }

    public int countArrangementWithMemo(int N) {
        if(N == 0)
            return 0;
        
        char[] used = new char[N + 1];
        Arrays.fill(used, 'n');
        Map<String, Integer> memory = new HashMap<>();
        return helper(N, 1, used, memory);
    }
    
    public int helper(int N, int pos, char[] used, Map<String, Integer> memory){
        if(pos > N){
            return 1;
        }
        String key = String.valueOf(used);
        if(memory.containsKey(key))
            return memory.get(key);
        int count = 0;
        for(int i = 1; i <= N; i++){
            if(used[i] == 'n' && (i % pos == 0 || pos % i == 0)){
                used[i] = 'y';
                count += helper(N, pos + 1, used, memory);
                used[i] = 'n';
            }
        }
        
        memory.put(key, count);
        return count;
    }
}

