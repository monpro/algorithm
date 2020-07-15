package strings;

class Pair {
    char c;
    int count;
    
    public Pair(char c, int count){
        this.c = c;
        this.count = count;
    }
}

class Solution {
    /**
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder builder = new StringBuilder();
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>(
        (p1, p2) -> p2.count - p1.count);
        
        if(a > 0){
            queue.add(new Pair('a', a));
        }
        if(b > 0){
            queue.add(new Pair('b', b));
        }
        if(c > 0){
            queue.add(new Pair('c', c));
        }
        
        while(queue.size() > 1){
            Pair first = queue.poll();
            
            if(first.count >= 2){
                builder.append(first.c);
                builder.append(first.c);
                first.count -= 2;
            }else{
                builder.append(first.c);
                first.count -= 1;
            }
            
            Pair second = queue.poll();
            if(second.count >= 2 && first.count < second.count){
                builder.append(second.c);
                builder.append(second.c);
                second.count -= 2;
            }else{
                builder.append(second.c);
                second.count -= 1;
            }
            
            if(first.count > 0){
                queue.add(first);
            }
            if(second.count > 0){
                queue.add(second);
            }
        }
        
        if(!queue.isEmpty()){
            if(builder.charAt(builder.length() - 1) != queue.peek().c){
                Pair pair = queue.peek();
                if(pair.count >= 2){
                    builder.append(pair.c);
                    builder.append(pair.c);
                }else{
                    builder.append(pair.c);
                }
            }
        }
        
        return builder.toString();
    }
    **/
    
    String generate(int a, int b, int c, String aa, String bb, String cc) {
    if (a < b)
        return generate(b, a, c, bb, aa, cc);
    if (a < c)
        return generate(c, b, a, cc, bb, aa);
    if (b < c)
        return generate(a, c, b, aa, cc, bb);
    if (b == 0)
        return aa.repeat(Math.min(2, a));
    int use_a = Math.min(2, a), use_b = a - use_a >= b ? 1 : 0; 
    return aa.repeat(use_a) + bb.repeat(use_b) +
        generate(a - use_a, b - use_b, c, aa, bb, cc);    
    }
    public String longestDiverseString(int a, int b, int c) {
        return generate(a, b, c, "a", "b", "c");
    }
}