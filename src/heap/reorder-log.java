package heap;

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> comparator = (log1, log2) -> {
            int log1SpaceIndex = log1.indexOf(" ");
            int log2SpaceIndex = log2.indexOf(" ");

            char log1ChAfterSpace = log1.charAt(log1SpaceIndex + 1);
            char log2ChAfterSpace = log2.charAt(log2SpaceIndex + 1);
            if(log1ChAfterSpace <= '9'){
                if(log2ChAfterSpace <= '9'){
                    return 0;
                }
                return 1;
            }

            if(log2ChAfterSpace <= '9'){
                return -1;
            }

            int subStringResult = log1.substring(log1SpaceIndex + 1).compareTo(log2.substring(log2SpaceIndex + 1));

            if(subStringResult == 0){
                return log1.substring(0, log1SpaceIndex).compareTo(log2.substring(0, log2SpaceIndex));
            }
            return subStringResult;
        };

        Arrays.sort(logs, comparator);
        return logs;
    }
}