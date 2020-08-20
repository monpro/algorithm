package strings;

import java.util.*;

class Solution {
    public String entityParser(String text) {
        String result = String.valueOf(text);
        Map<String, String> map = new HashMap<>();
        map.put("&quot;", "\"");
        map.put("&apos;", "'");
        map.put("&gt;", ">");
        map.put("&lt;", "<");
        map.put("&frasl;", "/");
        
        for(String key: map.keySet()) {
            result = result.replaceAll(key, map.get(key));
        }
        
        return result.replaceAll("&amp;", "&");
    }
}