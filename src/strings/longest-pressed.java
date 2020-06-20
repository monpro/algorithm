package strings;

class Solution {
    /*
    public boolean isLongPressedName(String name, String typed) {
        // index = 0, alex aallex 
        int indexName = 0, indexTyped = 0;
        char[] nameArr = name.toCharArray();
        char[] typedArr = typed.toCharArray();
        while(indexName < nameArr.length && indexTyped < typedArr.length){
            if(nameArr[indexName] == typedArr[indexTyped]){
                indexName += 1;
                indexTyped += 1;
            }
            else{
                if(indexTyped > 0 && typedArr[indexTyped] == typedArr[indexTyped - 1]){
                    indexTyped += 1;
                }
                else{
                    return false;
                }
            }
        }
        while(indexTyped > 0 && indexTyped < typedArr.length && typedArr[indexTyped] == typedArr[indexTyped - 1]){
            indexTyped += 1;
        }
        return indexName == nameArr.length && indexTyped == typedArr.length;
    }

    */
    
    public boolean isLongPressedName(String name, String typed) {
        int index = 0, m = name.length(), n = typed.length();
        
        for(int j = 0; j < n; j++){
            if(index < m && name.charAt(index) == typed.charAt(j)){
                index += 1;
            }
            else{
                if(j == 0 || typed.charAt(j) != typed.charAt(j - 1)){
                    return false;
                }
            }
        }
        return index == m;
    }
}