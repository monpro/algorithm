class MyCalendar {
    
    List<int[]> intervals;
    public MyCalendar() {
        intervals = new ArrayList<>();
    }
    
    public boolean book(int start, int end) {
        
        if(intervals.size() == 0){
            this.intervals.add(new int[]{start, end});
            return true;
        }
        
        int index = 0;
        while(index < intervals.size()){
            if(intervals.get(index)[0] >= end){
                this.intervals.add(index, new int[]{start, end});
                return true;
            }
            if(intervals.get(index)[1] > start && intervals.get(index)[0] < end){
                return false;
            }
            
            while(index < intervals.size() && intervals.get(index)[1] <= start){
                index ++;
            }
        }
        
        if(index == intervals.size()){
            this.intervals.add(new int[]{start, end});
            return true;
        }
        return false;
        
        
    }
}