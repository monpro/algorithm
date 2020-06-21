package designs;

import java.util.*;

class LFUCache {
    Map<Integer, Integer> counter;
    Map<Integer, Integer> freqs;
    Map<Integer, Set<Integer>> freqToKeys;
    int capacity = 0;
    int minFreq = -1;
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.counter = new HashMap<>();
        this.freqs = new HashMap<>();
        this.freqToKeys = new HashMap<>();
        freqToKeys.put(1, new LinkedHashSet<>());

    }
    
    public int get(int key) {
        if(!counter.containsKey(key)){
            return -1;
        }

        updateFreqs(key);
        return counter.get(key);
        
    }

    private void updateFreqs(int key){
        int freq = freqs.get(key);
        freqs.put(key, freq + 1);
        // remove this key from current freq group
        freqToKeys.get(freq).remove(key);
        
        if(freq == minFreq && freqToKeys.get(freq).size() == 0){
            minFreq += 1;
        }
        
        if(!freqToKeys.containsKey(freq + 1)){
            freqToKeys.put(freq + 1, new LinkedHashSet<>());
        }
        freqToKeys.get(freq + 1).add(key);
    }

    
    public void put(int key, int value) {
        if(capacity <= 0){
            return;
        }
        
        if(counter.containsKey(key)){
            counter.put(key, value);
            updateFreqs(key);
            return;
        }
        
        if(counter.size() >= capacity){
            int removeItem = freqToKeys.get(minFreq).iterator().next();
            freqToKeys.get(minFreq).remove(removeItem);
            counter.remove(removeItem);
        }
        
        counter.put(key, value);
        freqs.put(key, 1);
        minFreq = 1;
        freqToKeys.get(1).add(key);
        
        
    }
}