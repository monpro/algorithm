class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        Arrays.sort(deck);
        int[] result = new int[n];
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < n; i++)
            queue.add(i);
        
        for(int i = 0; i < n; i++){
            result[queue.poll()] = deck[i];
            queue.add(queue.poll());
        }
            
        return result;
        
    }
}