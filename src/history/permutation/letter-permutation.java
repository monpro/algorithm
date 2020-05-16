package history.permutation;

import java.util.*;

class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        if (S.length() == 0)
            return result;
        helper(S.toCharArray(), 0, result);
        return result;
    }

    public void helper(char[] array, int index, List<String> result) {
        if (index == array.length) {
            result.add(String.valueOf(array));
            return;
        }

        char c = array[index];
        if (Character.isLetter(c)) {
            array[index] = Character.toUpperCase(c);
            helper(array, index + 1, result);
            array[index] = Character.toLowerCase(c);
            helper(array, index + 1, result);
        } else {
            helper(array, index + 1, result);
        }
    }

    public List<String> findLetterCaseStringPermutations(String str) {
        List<String> permutations = new ArrayList<>();
        if (str == null) {
            return permutations;
        }
        permutations.add(str);

        for (int i = 0; i < str.length(); i++) {
            if (Character.isLetter(str.charAt(i))) {
                int size = permutations.size();

                for (int j = 0; j < size; j++) {
                    char[] arr = permutations.get(j).toCharArray();

                    if (Character.isUpperCase(arr[i])) {
                        arr[i] = Character.toLowerCase(arr[i]);
                    } else {
                        arr[i] = Character.toUpperCase(arr[i]);
                    }

                    permutations.add(String.valueOf(arr));
                }
            }
        }

        return permutations;
    }
}