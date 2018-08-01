package double_pointer;

public class valid_palindrome {
    public boolean isPalindrome(String s) {
        if(s.length() == 0){
            return true;
        }
        int left = 0, right = s.length() - 1;
        while (left < right){
            while (left < right && !isAlpha(s.charAt(left))){
                left++;
            }
            while (left < right && !isAlpha(s.charAt(right))){
                right--;
            }
            if(Character.toUpperCase(s.charAt(left)) != Character.toUpperCase(s.charAt(right))){
                return false;
            }
            left++;
            right--;
        }
        return true;

    }

    public boolean isAlpha(char c){
        return Character.isLetter(c) || Character.isDigit(c);
    }
}
