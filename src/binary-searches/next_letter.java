class NextLetter {

    public static char searchNextLetter(char[] letters, char key) {
      int n = letters.length;
      if(key < letters[0] || key > letters[n - 1]){
        return letters[0];
      }
  
      int start = 0, end = letters.length - 1;
      while(start <= end){
        int mid = start + (end - start) / 2;
  
        if(letters[mid] - key > 0){
          end -= 1;
        }else{
          start += 1;
        }
      }
      return letters[start];
    }
  
    public static void main(String[] args) {
      System.out.println(NextLetter.searchNextLetter(new char[] { 'a', 'c', 'f', 'h' }, 'f'));
      System.out.println(NextLetter.searchNextLetter(new char[] { 'a', 'c', 'f', 'h' }, 'b'));
      System.out.println(NextLetter.searchNextLetter(new char[] { 'a', 'c', 'f', 'h' }, 'm'));
      System.out.println(NextLetter.searchNextLetter(new char[] { 'a', 'c', 'f', 'h' }, 'h'));
    }
  }