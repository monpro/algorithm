class Solution {
    public List<Integer> splitIntoFibonacci(String S) {
        int n = S.length();
        
        for(int i = 1; i <= n / 2; i++){
            for(int j = 1; Math.max(i, j) <= n - i - j; j++){
                List<Integer> list = helper(i, j, S);
                if(list.size() > 0)
                    return list;
            }
        }
        
        return new ArrayList<>();
    }
    
    public boolean overFlow(String s){
        return s.length() > 10 || Long.parseLong(s) > Integer.MAX_VALUE;
    }
    
    public List<Integer> helper(int i, int j, String S){
        if(S.charAt(0) == '0' && i > 1)
            return new ArrayList<>();
        if(S.charAt(i) == '0' && j > 1)
            return new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        String sum;
        String s1 = S.substring(0, i);
        String s2 = S.substring(i, i+j);
        if(overFlow(s1) || overFlow(s2))            
            return new ArrayList<>();
        Long x1 = Long.parseLong(S.substring(0, i));
        Long x2 = Long.parseLong(S.substring(i, i+j));
        list.add(x1.intValue());
        list.add(x2.intValue());
        
        for(int start = i + j; start < S.length(); start += sum.length()){
            x2 = x1 + x2;
            x1 = x2 - x1;
            sum = x2.toString();
            if(overFlow(sum))
                return new ArrayList<>();
            if(S.startsWith(sum, start))
                list.add(x2.intValue());
            else
                return new ArrayList<>();
        }
        
        return list;
    }
}