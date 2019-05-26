package String;

import java.util.Map;

public class Longest_Common_Prefix_14 {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        String prefix = strs[0];
        for(int i = 1; i < strs.length; i++){
            while (strs[i].indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() - 1);

            }
        }
        return prefix;
    }
    public String longestCommonPrefix(String[] strs, int index){
        if(strs.length == 0) return "";
        for(int i = 0; i < strs.length; i++){
            char c = strs[0].charAt(i);
            for(int j = 1; j < strs.length; j++){
                if(j == strs.length || strs[j].charAt(i) != c){
                    return strs[0].substring(0,i);
                }
            }
        }

        return strs[0];
    }

    public String longestCommonPrefixWithDivideAndConquer(String[] strs){
        if(strs.length == 0) return "";
        return longestCommonPrefix(strs,0, strs.length - 1);
    }
    private String longestCommonPrefix(String[] strs, int left, int right) {
        if(left == right) return strs[left];
        int mid = (left + right) / 2;
        String lcpLeft = longestCommonPrefix(strs,left,mid);
        String lcpRight = longestCommonPrefix(strs, mid + 1, right);

        return commonPrefix(lcpLeft, lcpRight);
    }

    private String commonPrefix(String lcpLeft, String lcpRight){
        int minLengh = Math.min(lcpLeft.length(), lcpRight.length());
        for(int i = 0; i < minLengh; i++){
            if(lcpLeft.charAt(i) != lcpRight.charAt(i)){
                return lcpLeft.substring(0, i);
            }
        }
        return lcpLeft.substring(0, minLengh);
    }

    public static void main(String[] args){
        System.out.println("abcdabc".indexOf("abc"));
    }
}


