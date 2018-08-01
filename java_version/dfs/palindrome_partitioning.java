package dfs;

import java.util.ArrayList;
import java.util.List;

public class palindrome_partitioning {
    public List<List<String>> partition(String s) {
        // write your code here
        List<List<String>> results = new ArrayList<>();
        List<String> subset = new ArrayList<>();

        helper(results,subset,s,0);
        return results;
    }

    void helper(List<List<String>> results, List<String> subset, String s, int position){
        if(position == s.length()){
            results.add(subset);
            return;
        }

        for(int i = position; i < s.length();i++){
            String substring = s.substring(position,i+1);
            if(!is_palindrome(substring)){
                continue;
            }
            subset.add(substring);
            helper(results,new ArrayList<>(subset),s,i + 1);
            subset.remove(subset.size() - 1);
        }
    }

    boolean is_palindrome(String string){
        int left = 0;
        int right = string.length() -1;

        while(left < right){
            if(string.charAt(left) != string.charAt(right)){
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;

    }
}
