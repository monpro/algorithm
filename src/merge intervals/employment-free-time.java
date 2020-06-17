import java.util.*;

class Interval {
  int start;
  int end;

  public Interval(int start, int end) {
    this.start = start;
    this.end = end;
  }
};

class EmployeeInterval {
  Interval interval;
  int employeeIndex;
  int intervalIndex;

  public EmployeeInterval(Interval interval, int employeeIndex, int intervalIndex){
    this.interval = interval;
    this.employeeIndex = employeeIndex;
    this.intervalIndex = intervalIndex;
  }
}

class EmployeeFreeTime {

  public static List<Interval> findEmployeeFreeTime(List<List<Interval>> schedule) {
    List<Interval> result = new ArrayList<>();
    PriorityQueue<EmployeeInterval> minHeap = new PriorityQueue<>((a, b) -> a.interval.start - b.interval.start);

    for(int i = 0; i < schedule.size(); i++){
      minHeap.add(new EmployeeInterval(schedule.get(i).get(0), i, 0));
    }

    Interval previousInterval = minHeap.peek().interval;

    while(!minHeap.isEmpty()){
      EmployeeInterval nextInterval = minHeap.poll();
      if(previousInterval.end < nextInterval.interval.start){
        result.add(new Interval(previousInterval.end, nextInterval.interval.start));
        previousInterval = nextInterval.interval;
      }else{
        if(previousInterval.end < nextInterval.interval.end){
          previousInterval = nextInterval.interval;
        }
      }

      List<Interval> employee = schedule.get(nextInterval.employeeIndex);

      if(employee.size() > nextInterval.intervalIndex + 1){
        minHeap.offer(new EmployeeInterval(employee.get(nextInterval.intervalIndex + 1), nextInterval.employeeIndex, nextInterval.intervalIndex + 1));
      }

    }

    return result;
  }