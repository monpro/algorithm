class Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length() - 1, j = T.length() - 1;
        
        while(i >= 0 || j >= 0){
            int index1 = nextValidIndex(S, i);
            int index2 = nextValidIndex(T, j);
            
            if(index1 < 0 && index2 < 0)
                return true;
            else if(index1 < 0 || index2 < 0)
                return false;
            else if(S.charAt(index1) != T.charAt(index2))
                return false;
            i = index1 - 1;
            j = index2 - 1;
        }
        return true;
    }
    
    
    private int nextValidIndex(String S, int index){
        int backspace = 0;
        while(index >= 0){
            if(S.charAt(index) == '#'){
                backspace += 1;
            }else if(backspace > 0){
                backspace -= 1;
            }else{
                break;
            }
            index -= 1;
        }
        return index;
    }
}