class Solution {
    public boolean isHappy(int num) {
        int slow = num, fast = num;
        do{
          slow = findNextNum(slow);
          fast = findNextNum(findNextNum(fast));
        }while(slow != fast);

        return fast == 1;
  }

  private int findNextNum(int num){
    int result = 0, digit;
    while(num > 0){
      digit = num % 10;
      result += digit * digit;
      num /= 10;
    }
    return result;
  }
}