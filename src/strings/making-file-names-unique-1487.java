package strings;

import java.util.*;

class Solution {
    public String[] getFolderNames(String[] names) {
        Map<String, Integer> map = new HashMap<>();
        int n = names.length;
        String[] result = new String[n];
        
        for(int i = 0; i < n; i++){
            if(!map.containsKey(names[i])) {
                result[i] = names[i];
                map.put(names[i], 1);
            } else {
                int suffix = map.get(names[i]);
                String name = names[i] + "(" + suffix + ")";
                while(map.containsKey(name)) {
                    suffix += 1;
                    name = names[i] + "(" + suffix + ")";
                }
                result[i] = name;
                // update names suffix [php, php(1), php] suffix - 2
                map.put(names[i], ++suffix);
                // update name suffix [php, php(1), php(1), php(1)(1)];
                // [php, php(1), php(1)(1), php(1)(1)(1)]
                map.put(name, 1);
            }
        }
        return result;
    }
}