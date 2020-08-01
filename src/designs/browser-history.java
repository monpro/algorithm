package designs;

import java.util.*;

/**
 * class BrowserHistory { Stack<String> back; Stack<String> forward; String cur;
 * public BrowserHistory(String homepage) { cur = homepage; back = new
 * Stack<>(); forward = new Stack<>(); }
 * 
 * public void visit(String url) { forward = new Stack<>(); back.add(cur); cur =
 * url; }
 * 
 * public String back(int steps) { while(steps > 0 && !back.isEmpty()) {
 * forward.add(cur); cur = back.pop(); steps -= 1; }
 * 
 * return cur; }
 * 
 * public String forward(int steps) { while(steps > 0 && !forward.isEmpty()) {
 * back.add(cur); cur = forward.pop(); steps -= 1; } return cur; } }
 **/

class BrowserHistory {
    List<String> list;
    int index = 0;
    public BrowserHistory(String homepage) {
        list = new LinkedList<>();
        list.add(homepage);
    }
    
    public void visit(String url) {
        list.subList(index + 1, list.size()).clear();
        list.add(url);
        index += 1;
    }
    
    public String back(int steps) {
        index = index - steps < 0 ? 0: index - steps;
        return list.get(index);
    }
    
    public String forward(int steps) {
        index = index + steps > list.size() - 1? list.size() - 1: index + steps;
        return list.get(index);
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */