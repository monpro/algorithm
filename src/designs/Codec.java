package designs;

import java.util.*;

public class Codec {

    // Encodes a URL to a shortened URL.
    Map<Integer, String> map = new HashMap<>();
    String host = "http://tinyurl.com/";
    
    
    public String encode(String longUrl) {
        int key = longUrl.hashCode();
        map.put(key, longUrl);
        
        return host + key;
        
    }
        
    
    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        int key = Integer.parseInt(shortUrl.replace(host, ""));
        return map.get(key);
    }
}