class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        if(S.length() == 0)
            return result;
        helper(S.toCharArray(), 0, result);
        return result;
    }
    
    public void helper(char[] array, int index, List<String> result){
        if(index == array.length){
            result.add(String.valueOf(array));
            return;
        }
        
        char c = array[index];
        if(Character.isLetter(c)){
            array[index] = Character.toUpperCase(c);
            helper(array, index + 1, result);
            array[index] = Character.toLowerCase(c);
            helper(array, index + 1, result);
        }
        else{
            helper(array, index + 1, result);
        }
    }
}