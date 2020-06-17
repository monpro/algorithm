class Meeting {
  int start;
  int end;

  public Meeting(int start, int end) {
    this.start = start;
    this.end = end;
  }
};

class MinimumMeetingRooms {

  public static int findMinimumMeetingRooms(List<Meeting> meetings) {
    if(meetings == null || meetings.size() == 0){
      return 0;
    }

    Collections.sort(meetings, (a, b) -> a.start - b.start);

    PriorityQueue<Meeting> minHeap = new PriorityQueue<>(meetings.size(), (a, b) -> a.end - b.end);
    int size = 0;
    for(Meeting meeting: meetings){
      while(!minHeap.isEmpty() && meeting.start >= minHeap.peek().end){
        minHeap.poll();
      }
      minHeap.offer(meeting);

      size = Math.max(size, minHeap.size());

    }
    return size;
  }