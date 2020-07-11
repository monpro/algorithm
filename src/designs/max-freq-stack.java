package designs;

import java.util.*;

class FreqStack {

    Map<Integer, Integer> freq;
    Map<Integer, Stack<Integer>> freqMapStack;
    int maxFreq;
    public FreqStack() {
        freq = new HashMap<>();
        freqMapStack = new HashMap<>();
        maxFreq = 0;
    }
    
    public void push(int x) {
        int curFreq = freq.getOrDefault(x, 0) + 1;
        maxFreq = Math.max(curFreq, maxFreq);
        freq.put(x, curFreq);
        freqMapStack.putIfAbsent(curFreq, new Stack<Integer>());
        freqMapStack.get(curFreq).add(x);
        
    }
    
    public int pop() {
        int ele = freqMapStack.get(maxFreq).pop();
        freq.put(ele, freq.get(ele) - 1);
        if(freqMapStack.get(maxFreq).size() == 0){
            maxFreq -= 1;
        }
        
        return ele;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */